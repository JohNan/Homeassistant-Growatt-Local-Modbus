"""Growatt Sensor definitions for the Inverter type."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorStateClass,
)
from homeassistant.const import (
    ELECTRIC_CURRENT_AMPERE,
    ELECTRIC_POTENTIAL_VOLT,
    ENERGY_KILO_WATT_HOUR,
    FREQUENCY_HERTZ,
    POWER_WATT,
    TEMP_CELSIUS,
    TIME_HOURS,
    PERCENTAGE,
)
from .sensor_entity_description import GrowattSensorEntityDescription
from .switch_entity_description import GrowattSwitchEntityDescription

# relative import NOT WORKING due to into higher located reference
# from .growatt_local.API.device_type.base import ATTR

# Attribute names for values in the holding register

ATTR_FIRMWARE = "firmware"
ATTR_SERIAL_NUMBER = "serial number"
ATTR_INVERTER_MODEL = "Inverter model"

ATTR_DEVICE_TYPE_CODE = "device type code"
ATTR_NUMBER_OF_TRACKERS_AND_PHASES = "number of trackers and phases"

ATTR_MODBUS_VERSION = "modbus version"

# Attribute names for values in the input register

ATTR_STATUS = "status"
ATTR_STATUS_CODE = "status_code"
ATTR_DERATING_MODE = "derating_mode"
ATTR_FAULT_CODE = "fault_code"
ATTR_WARNING_CODE = "warning_code"
ATTR_WARNING_VALUE = "warning_value"

ATTR_INPUT_POWER = "input_power"  # W
ATTR_INPUT_ENERGY_TOTAL = "input_energy_total"  # kWh

ATTR_INPUT_1_VOLTAGE = "input_1_voltage"  # V
ATTR_INPUT_1_AMPERAGE = "input_1_amperage"  # A
ATTR_INPUT_1_POWER = "input_1_power"  # W
ATTR_INPUT_1_ENERGY_TODAY = "input_1_energy_today"  # kWh
ATTR_INPUT_1_ENERGY_TOTAL = "input_1_energy_total"  # kWh

ATTR_INPUT_2_VOLTAGE = "input_2_voltage"  # V
ATTR_INPUT_2_AMPERAGE = "input_2_amperage"  # A
ATTR_INPUT_2_POWER = "input_2_power"  # W
ATTR_INPUT_2_ENERGY_TODAY = "input_2_energy_today"  # kWh
ATTR_INPUT_2_ENERGY_TOTAL = "input_2_energy_total"  # kWh

ATTR_INPUT_3_VOLTAGE = "input_3_voltage"  # V
ATTR_INPUT_3_AMPERAGE = "input_3_amperage"  # A
ATTR_INPUT_3_POWER = "input_3_power"  # W
ATTR_INPUT_3_ENERGY_TODAY = "input_3_energy_today"  # kWh
ATTR_INPUT_3_ENERGY_TOTAL = "input_3_energy_total"  # kWh

ATTR_INPUT_4_VOLTAGE = "input_4_voltage"  # V
ATTR_INPUT_4_AMPERAGE = "input_4_amperage"  # A
ATTR_INPUT_4_POWER = "input_4_power"  # W
ATTR_INPUT_4_ENERGY_TODAY = "input_4_energy_today"  # kWh
ATTR_INPUT_4_ENERGY_TOTAL = "input_4_energy_total"  # kWh

ATTR_INPUT_5_VOLTAGE = "input_5_voltage"  # V
ATTR_INPUT_5_AMPERAGE = "input_5_amperage"  # A
ATTR_INPUT_5_POWER = "input_5_power"  # W
ATTR_INPUT_5_ENERGY_TODAY = "input_5_energy_today"  # kWh
ATTR_INPUT_5_ENERGY_TOTAL = "input_5_energy_total"  # kWh

ATTR_INPUT_6_VOLTAGE = "input_6_voltage"  # V
ATTR_INPUT_6_AMPERAGE = "input_6_amperage"  # A
ATTR_INPUT_6_POWER = "input_6_power"  # W
ATTR_INPUT_6_ENERGY_TODAY = "input_6_energy_today"  # kWh
ATTR_INPUT_6_ENERGY_TOTAL = "input_6_energy_total"  # kWh

ATTR_INPUT_7_VOLTAGE = "input_7_voltage"  # V
ATTR_INPUT_7_AMPERAGE = "input_7_amperage"  # A
ATTR_INPUT_7_POWER = "input_7_power"  # W
ATTR_INPUT_7_ENERGY_TODAY = "input_7_energy_today"  # kWh
ATTR_INPUT_7_ENERGY_TOTAL = "input_7_energy_total"  # kWh

ATTR_INPUT_8_VOLTAGE = "input_8_voltage"  # V
ATTR_INPUT_8_AMPERAGE = "input_8_amperage"  # A
ATTR_INPUT_8_POWER = "input_8_power"  # W
ATTR_INPUT_8_ENERGY_TODAY = "input_8_energy_today"  # kWh
ATTR_INPUT_8_ENERGY_TOTAL = "input_8_energy_total"  # kWh

ATTR_OUTPUT_POWER = "output_power"  # W
ATTR_OUTPUT_ENERGY_TODAY = "output_energy_today"  # kWh
ATTR_OUTPUT_ENERGY_TOTAL = "output_energy_total"  # kWh

ATTR_OUTPUT_REACTIVE_POWER = "output_reactive_power"  # Var
ATTR_OUTPUT_REACTIVE_ENERGY_TODAY = "output_reactive_energy_today"  # kVarh
ATTR_OUTPUT_REACTIVE_ENERGY_TOTAL = "output_reactive_energy_total"  # kVarh

ATTR_OUTPUT_1_VOLTAGE = "output_1_voltage"  # V
ATTR_OUTPUT_1_AMPERAGE = "output_1_amperage"  # A
ATTR_OUTPUT_1_POWER = "output_1_power"  # W

ATTR_OUTPUT_2_VOLTAGE = "output_2_voltage"  # V
ATTR_OUTPUT_2_AMPERAGE = "output_2_amperage"  # A
ATTR_OUTPUT_2_POWER = "output_2_power"  # W

ATTR_OUTPUT_3_VOLTAGE = "output_3_voltage"  # V
ATTR_OUTPUT_3_AMPERAGE = "output_3_amperage"  # A
ATTR_OUTPUT_3_POWER = "output_3_power"  # W

ATTR_OPERATION_HOURS = "operation_hours"  # s

ATTR_FREQUENCY = "frequency"  # Hz

ATTR_TEMPERATURE = "inverter_temperature"  # C
ATTR_IPM_TEMPERATURE = "ipm_temperature"  # C
ATTR_BOOST_TEMPERATURE = "boost_temperature"  # C

ATTR_P_BUS_VOLTAGE = "p_bus_voltage"  # V
ATTR_N_BUS_VOLTAGE = "n_bus_voltage"  # V

ATTR_OUTPUT_PERCENTAGE = "real_output_power_percent"  # %

# 1.24 registers
ATTR_SOC_PERCENTAGE = "soc"  # %
ATTR_DISCHARGE_POWER = "discharge_power"  # W
ATTR_CHARGE_POWER = "charge_power"  # W
ATTR_ENERGY_TO_USER_TODAY = "energy_to_user_today"  # kWh
ATTR_ENERGY_TO_USER_TOTAL = "energy_to_user_total"  # kWh
ATTR_ENERGY_TO_GRID_TODAY = "energy_to_grid_today"  # kWh
ATTR_ENERGY_TO_GRID_TOTAL = "energy_to_grid_total"  # kWh
ATTR_DISCHARGE_ENERGY_TODAY = "discharge_energy_today"  # kWh
ATTR_DISCHARGE_ENERGY_TOTAL = "discharge_energy_total"  # kWh
ATTR_CHARGE_ENERGY_TODAY = "charge_energy_today"  # kWh
ATTR_CHARGE_ENERGY_TOTAL = "charge_energy_total"  # kWh
ATTR_AC_CHARGE_ENABLED = "ac_charge_enabled"  # bool / binary
ATTR_TIME_1 = "time_1" 

INVERTER_SWITCH_TYPES: tuple[GrowattSwitchEntityDescription, ...] = (
    GrowattSwitchEntityDescription(
        key=ATTR_AC_CHARGE_ENABLED,
        name="AC Charge"
    ),
)

INVERTER_SENSOR_TYPES: tuple[GrowattSensorEntityDescription, ...] = (
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_ENERGY_TODAY,
        name="Energy produced today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_ENERGY_TOTAL,
        name="Total energy produced",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_ENERGY_TOTAL,
        name="Total energy input",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_1_VOLTAGE,
        name="Input 1 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_1_AMPERAGE,
        name="Input 1 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_1_POWER,
        name="Input 1 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_1_ENERGY_TODAY,
        name="Input 1 energy today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_1_ENERGY_TOTAL,
        name="Input 1 total energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_2_VOLTAGE,
        name="Input 2 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_2_AMPERAGE,
        name="Input 2 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_2_POWER,
        name="Input 2 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_2_ENERGY_TODAY,
        name="Input 2 energy today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_2_ENERGY_TOTAL,
        name="Input 2 total energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_3_VOLTAGE,
        name="Input 3 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_3_AMPERAGE,
        name="Input 3 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_3_POWER,
        name="Input 3 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_3_ENERGY_TODAY,
        name="Input 3 energy today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_3_ENERGY_TOTAL,
        name="Input 3 total energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_4_VOLTAGE,
        name="Input 4 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_4_AMPERAGE,
        name="Input 4 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_4_POWER,
        name="Input 4 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_4_ENERGY_TODAY,
        name="Input 4 energy today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_4_ENERGY_TOTAL,
        name="Input 4 total energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_5_VOLTAGE,
        name="Input 5 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_5_AMPERAGE,
        name="Input 5 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_5_POWER,
        name="Input 5 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_5_ENERGY_TODAY,
        name="Input 5 energy today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_5_ENERGY_TOTAL,
        name="Input 5 total energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_6_VOLTAGE,
        name="Input 6 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_6_AMPERAGE,
        name="Input 6 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_6_POWER,
        name="Input 6 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_6_ENERGY_TODAY,
        name="Input 6 energy today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_6_ENERGY_TOTAL,
        name="Input 6 total energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_7_VOLTAGE,
        name="Input 7 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_7_AMPERAGE,
        name="Input 7 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_7_POWER,
        name="Input 7 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_7_ENERGY_TODAY,
        name="Input 7 energy today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_7_ENERGY_TOTAL,
        name="Input 7 total energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_8_VOLTAGE,
        name="Input 8 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_8_AMPERAGE,
        name="Input 8 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_8_POWER,
        name="Input 8 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_8_ENERGY_TODAY,
        name="Input 8 energy today",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_8_ENERGY_TOTAL,
        name="Input 8 total energy",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_1_VOLTAGE,
        name="Output 1 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_1_AMPERAGE,
        name="Output 1 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_1_POWER,
        name="Output 1 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_2_VOLTAGE,
        name="Output 2 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_2_AMPERAGE,
        name="Output 2 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_2_POWER,
        name="Output 2 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_3_VOLTAGE,
        name="Output 3 voltage",
        native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
        device_class=SensorDeviceClass.VOLTAGE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_3_AMPERAGE,
        name="Output 3 Amperage",
        native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
        device_class=SensorDeviceClass.CURRENT,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_3_POWER,
        name="Output 3 Wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OPERATION_HOURS,
        name="Running hours",
        native_unit_of_measurement=TIME_HOURS,
        device_class=SensorDeviceClass.DURATION,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_INPUT_POWER,
        name="Internal wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_FREQUENCY,
        name="AC frequency",
        native_unit_of_measurement=FREQUENCY_HERTZ,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_POWER,
        name="Output power",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_REACTIVE_POWER,
        name="Reactive wattage",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_IPM_TEMPERATURE,
        name="Intelligent Power Management temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_TEMPERATURE,
        name="Temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=SensorDeviceClass.TEMPERATURE,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_OUTPUT_PERCENTAGE,
        name="Real power output percentage",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.POWER_FACTOR
    ),
    GrowattSensorEntityDescription(
        key=ATTR_SOC_PERCENTAGE,
        name="SOC",
        native_unit_of_measurement=PERCENTAGE,
        device_class=SensorDeviceClass.BATTERY
    ),
    GrowattSensorEntityDescription(
        key=ATTR_DISCHARGE_POWER,
        name="Discharge Power",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER
    ),
    GrowattSensorEntityDescription(
        key=ATTR_CHARGE_POWER,
        name="Charge Power",
        native_unit_of_measurement=POWER_WATT,
        device_class=SensorDeviceClass.POWER
    ),
    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_GRID_TOTAL,
        name="Energy To Grid (Total)",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_GRID_TODAY,
        name="Energy To Grid (Today)",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_USER_TOTAL,
        name="Energy To User (Total)",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),

    GrowattSensorEntityDescription(
        key=ATTR_ENERGY_TO_USER_TODAY,
        name="Energy To User (Today)",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_AC_CHARGE_ENABLED,
        name="AC Charge Enabled"
    ),
    GrowattSensorEntityDescription(
        key=ATTR_TIME_1,
        name="Time 1"
    ),
    GrowattSensorEntityDescription(
        key=ATTR_DISCHARGE_ENERGY_TODAY,
        name="Battery Discharged (Today)",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_DISCHARGE_ENERGY_TOTAL,
        name="Battery Discharged (Total)",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
    ),
    GrowattSensorEntityDescription(
        key=ATTR_CHARGE_ENERGY_TODAY,
        name="Battery Charged (Today)",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,
        midnight_reset=True
    ),
    GrowattSensorEntityDescription(
        key=ATTR_CHARGE_ENERGY_TOTAL,
        name="Battery Charged (Total)",
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        device_class=SensorDeviceClass.ENERGY,
        state_class=SensorStateClass.TOTAL_INCREASING,

    ),
    GrowattSensorEntityDescription(
        key="status",
        name="Status",
        device_class=f"growatt_local__status"
    ),
)
