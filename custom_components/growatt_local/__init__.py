"""The Growatt server PV inverter sensor integration."""
import asyncio
import logging
from collections.abc import Callable, Sequence
from datetime import timedelta
from typing import Any, Optional

from pymodbus.exceptions import ConnectionException

from homeassistant import config_entries
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_ADDRESS,
    CONF_IP_ADDRESS,
    CONF_PORT,
    CONF_SCAN_INTERVAL,
    SUN_EVENT_SUNRISE,
    SUN_EVENT_SUNSET,
    EVENT_HOMEASSISTANT_STARTED,
)
from homeassistant.core import CALLBACK_TYPE, HomeAssistant, callback
from homeassistant.helpers.event import (
    async_track_sunrise,
    async_track_sunset,
    async_track_time_change,
)
from homeassistant.helpers.sun import get_astral_event_next
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
)
from homeassistant.util import dt as dt_util
from .API.device_type.base import GrowattDeviceRegisters
from .API.growatt import GrowattDevice, GrowattSerial, GrowattNetwork
from .const import (
    CONF_LAYER,
    CONF_SERIAL,
    CONF_SERIAL_NUMBER,
    CONF_TCP,
    CONF_UDP,
    CONF_SERIAL_PORT,
    CONF_BAUDRATE,
    CONF_BYTESIZE,
    CONF_PARITY,
    CONF_STOPBITS,
    CONF_POWER_SCAN_ENABLED,
    CONF_POWER_SCAN_INTERVAL,
    DOMAIN,
    PLATFORMS,
)

_LOGGER = logging.getLogger(__name__)

async def config_entry_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Update listener, called when the config entry options are changed."""
    await hass.config_entries.async_reload(entry.entry_id)

async def async_setup_entry(
    hass: HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Load the saved entities."""
    _LOGGER.warning(f"setup entries - data: {entry.data}, options: {entry.options}")
    options = entry.options
    
    if entry.data[CONF_LAYER] == CONF_SERIAL:
        device_layer = GrowattSerial(
            entry.data[CONF_SERIAL_PORT],
            entry.data[CONF_BAUDRATE],
            entry.data[CONF_STOPBITS],
            entry.data[CONF_PARITY],
            entry.data[CONF_BYTESIZE],
        )
    elif entry.data[CONF_LAYER] in (CONF_TCP, CONF_UDP):
        device_layer = GrowattNetwork(
            entry.data[CONF_LAYER],
            options.get(CONF_IP_ADDRESS, data.get(CONF_IP_ADDRESS, None)),
            entry.data[CONF_PORT],
        )
    else:
        _LOGGER.warning(
            "Device layer %s is not supported right now",
            entry.data[CONF_LAYER],
        )
        return False

    device = GrowattDevice(
        device_layer, entry.data[CONF_ADDRESS]
    )

    coordinator = GrowattLocalCoordinator(
        hass,
        device,
        timedelta(seconds=entry.data[CONF_SCAN_INTERVAL]),
        timedelta(seconds=entry.data[CONF_POWER_SCAN_INTERVAL])
        if entry.data[CONF_POWER_SCAN_ENABLED]
        else None,
    )

    hass.data.setdefault(DOMAIN, {})[entry.data[CONF_SERIAL_NUMBER]] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    if hass.is_running:
        await device.connect()
    else:
        hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STARTED, device.connect)
    
    entry.async_on_unload(entry.add_update_listener(config_entry_update_listener))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    await hass.data[DOMAIN][entry.data[CONF_SERIAL_NUMBER]].growatt_api.close()

    if unload_ok:
        hass.data[DOMAIN].pop(entry.data[CONF_SERIAL_NUMBER])
    return unload_ok


class GrowattLocalCoordinator(DataUpdateCoordinator):
    """My custom coordinator."""

    def __init__(
        self,
        hass: HomeAssistant,
        growatt_api: GrowattDevice,
        update_interval: timedelta,
        power_interval: Optional[timedelta] = None,
    ) -> None:
        """Initialize my coordinator."""
        self.interval = power_interval if power_interval else update_interval
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            # Polling interval. Will only be polled if there are subscribers.
            update_interval=self.interval,
        )
        self.data = {}
        self.growatt_api = growatt_api
        self._failed_update_count = 0
        self.keys = set()
        self.holding_keys = set()
        self.p_keys = set()
        self._midnight_listeners: dict[
            CALLBACK_TYPE, tuple[CALLBACK_TYPE, object | None]
        ] = {}

        if power_interval:
            self._counter = self._max_counter = update_interval / power_interval
        else:
            self._counter = self._max_counter = 0

        self._sun_is_down = self.sun_down()

        async_track_sunrise(self.hass, self.sunrise)
        async_track_sunset(self.hass, self.sunset, timedelta(minutes=-10))

        async_track_time_change(self.hass, self.midnight, 0, 0, 0)

    @callback
    def async_update_listeners(self) -> None:
        """Update only the registered listeners for which we have new data."""
        for update_callback, context in set(self._listeners.values()):
            if context in self.data.keys():
                update_callback()

    async def _async_update_data(self):
        """Fetch data from API endpoint.

        This is the place to pre-process the data to lookup tables
        so entities can quickly look up their data.
        """
        status = None
        data = {}

#        if self._sun_is_down:
 #           return {"status": "Offline"}
        try:
            if self._counter >= self._max_counter or self._failed_update_count > 0:
                self._counter = 0
                data = await self.growatt_api.update(self.keys)
                holding_data = await self.growatt_api.update_holding(self.holding_keys)
                data.update(holding_data)
                _LOGGER.debug(f"Updated data: {data}")
            else:
                self._counter += 1
                data = await self.growatt_api.update(self.p_keys)
            self._failed_update_count = 0
        except ConnectionException:
            self._failed_update_count += 1
            status = "not_connected"
        except asyncio.TimeoutError:
            self._failed_update_count += 1
            status = "no_response"

        if status is None:
            status = self.growatt_api.status(data)

        if status:
            data["status"] = status

        return data

    async def force_refresh(self):
        self._counter = 999
        await self.async_request_refresh()
        
    async def sunrise(self):
        """Callback function when sunrise occours."""
        _LOGGER.info("System waking up on sunrise")
        self.update_interval = self.interval
        self._sun_is_down = False
        await self.async_request_refresh()

    async def sunset(self):
        """Callback function when sunset occours."""
        _LOGGER.info("System going into sleep mode")
        self._sun_is_down = True
        await self.async_request_refresh()
        self.update_interval = timedelta(hours=1)
        self._failed_update_count = 0
        self._counter = 0

    def sun_down(self) -> bool:
        """Customized datetimes and inversion for the implemented sun_up function of home assistant"""

        utc_point_in_time = dt_util.utcnow()

        next_sunrise = get_astral_event_next(
            self.hass, SUN_EVENT_SUNRISE, utc_point_in_time + timedelta(minutes=5)
        )
        next_sunset = get_astral_event_next(
            self.hass, SUN_EVENT_SUNSET, utc_point_in_time + timedelta(minutes=15)
        )

        return next_sunrise < next_sunset

    @callback
    def midnight(self, datetime=None):
        for update_callback, context in set(self._midnight_listeners.values()):
            self.data.update({context: 0})
            update_callback()

    @callback
    def async_add_midnight_listener(
        self, update_callback: CALLBACK_TYPE, context: Any = None
    ) -> Callable[[], None]:
        """Listeners for midnight update."""
        schedule_refresh = not self._midnight_listeners

        @callback
        def remove_midnight_listener() -> None:
            """Remove midnight listener."""
            self._midnight_listeners.pop(remove_midnight_listener)
            if not self._midnight_listeners:
                # determine if time track can be removed
                pass

        self._midnight_listeners[remove_midnight_listener] = (update_callback, context)

        # This is the first listener, set up interval.
        if schedule_refresh:
            async_track_time_change(self.hass, self.midnight, 0, 0, 0)

        return remove_midnight_listener

    @callback
    def get_keys_by_name(
        self, names: Sequence[str], update_keys: bool = False
    ) -> set[int]:
        """
        Loopup modbus register values based on name.
        Setting update_keys automaticly extends the list of keys to request.
        """
        keys = self.growatt_api.get_keys_by_name(names)
        if update_keys:
            self.keys.update(keys)

        return keys

    @callback
    def get_holding_keys_by_name(
        self, names: Sequence[str], update_keys: bool = False
    ) -> set[int]:
        """
        Loopup modbus register values based on name.
        Setting update_keys automaticly extends the list of keys to request.
        """
        keys = self.growatt_api.get_holding_keys_by_name(names)
        if update_keys:
            self.holding_keys.update(keys)

        return keys

    def get_register_by_name(self, name) -> GrowattDeviceRegisters:
        return self.growatt_api.get_register_by_name(name)

    def get_holding_register_by_name(self, name) -> GrowattDeviceRegisters:
        return self.growatt_api.get_holding_register_by_name(name)

    async def write_register(self, register, payload):
        await self.growatt_api.write_register(register, payload)
