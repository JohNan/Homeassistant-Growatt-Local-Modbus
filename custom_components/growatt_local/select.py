import logging
from datetime import timedelta

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_MODEL,
    CONF_NAME,
    CONF_TYPE,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
)
from .API.const import DeviceTypes
from .const import (
    CONF_FIRMWARE,
    CONF_SERIAL_NUMBER,
    DOMAIN,
)
from .sensor_types.inverter import INVERTER_SELECT_TYPES
from .sensor_types.select_entity_description import GrowattSelectEntityDescription

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=1)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:

    coordinator = hass.data[DOMAIN][config_entry.data[CONF_SERIAL_NUMBER]]

    entities = []
    sensor_descriptions: list[GrowattSelectEntityDescription] = []

    device_type = DeviceTypes(config_entry.data[CONF_TYPE])

    if device_type in (DeviceTypes.INVERTER, DeviceTypes.INVERTER_315, DeviceTypes.INVERTER_120, DeviceTypes.INVERTER_124):
        supported_key_names = coordinator.growatt_api.get_register_names()

        for sensor in INVERTER_SELECT_TYPES:
            if sensor.key not in supported_key_names:
                continue

            sensor_descriptions.append(sensor)

    else:
        _LOGGER.debug(
            "Device type %s was found but is not supported right now",
            config_entry.data[CONF_TYPE],
        )

    coordinator.get_keys_by_name({sensor.key for sensor in sensor_descriptions}, True)

    entities.extend(
        [
            GrowattDeviceEntity(
                coordinator, description=description, entry=config_entry
            )
            for description in sensor_descriptions
        ]
    )

    async_add_entities(entities, True)


class GrowattDeviceEntity(CoordinatorEntity, RestoreEntity, SelectEntity):
    """An entity using CoordinatorEntity."""

    def __init__(self, coordinator, description, entry):
        """Pass coordinator to CoordinatorEntity."""
        super().__init__(coordinator, description.key)
        self.entity_description: GrowattSelectEntityDescription = description
        self._attr_unique_id = (
            f"{DOMAIN}_{entry.data[CONF_SERIAL_NUMBER]}_{description.key}"
        )

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.data[CONF_SERIAL_NUMBER])},
            manufacturer="Growatt",
            model=entry.data[CONF_MODEL],
            sw_version=entry.data[CONF_FIRMWARE],
            name=entry.data[CONF_NAME],
        )

    @property
    def current_option(self) -> str:
        state = self.coordinator.data.get(self.entity_description.key)
        return self.entity_description.options_dict.get(state)

    async def async_select_option(self, option: str) -> None:
        key = self.coordinator.get_key_by_name(self.entity_description.key)
        await self.coordinator.write_register(key)

    async def async_added_to_hass(self) -> None:
        """Call when entity is about to be added to Home Assistant."""
        await super().async_added_to_hass()

        if self.entity_description.midnight_reset:
            self.async_on_remove(
                self.coordinator.async_add_midnight_listener(
                    self._handle_midnight_update, self.coordinator_context
                )
            )

        if (state := await self.async_get_last_state()) is None:
            return

        self._attr_native_value = state.state

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        if (state := self.coordinator.data.get(self.entity_description.key)) is None:
            return
        self._attr_native_value = state
        self.async_write_ha_state()

    @callback
    def _handle_midnight_update(self) -> None:
        """Handle updated data from the coordinator."""
        if (state := self.coordinator.data.get(self.entity_description.key)) is None:
            return
        self._attr_native_value = state
        self.async_write_ha_state()
