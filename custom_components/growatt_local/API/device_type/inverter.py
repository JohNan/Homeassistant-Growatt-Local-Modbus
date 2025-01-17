"""Device defaults for a Growatt Inverter."""
import logging
import datetime

from .base import (
    GrowattDeviceRegisters,
    custom_function,
    FIRMWARE_REGISTER,
    DEVICE_TYPE_CODE_REGISTER,
    NUMBER_OF_TRACKERS_AND_PHASES_REGISTER,
    ATTR_INVERTER_MODEL,
    ATTR_MODBUS_VERSION,
    ATTR_STATUS_CODE,
    ATTR_DERATING_MODE,
    ATTR_FAULT_CODE,
    ATTR_WARNING_CODE,
    ATTR_WARNING_VALUE,
    ATTR_INPUT_POWER,
    ATTR_INPUT_ENERGY_TOTAL,
    ATTR_INPUT_1_VOLTAGE,
    ATTR_INPUT_1_AMPERAGE,
    ATTR_INPUT_1_POWER,
    ATTR_INPUT_1_ENERGY_TODAY,
    ATTR_INPUT_1_ENERGY_TOTAL,
    ATTR_INPUT_2_VOLTAGE,
    ATTR_INPUT_2_AMPERAGE,
    ATTR_INPUT_2_POWER,
    ATTR_INPUT_2_ENERGY_TODAY,
    ATTR_INPUT_2_ENERGY_TOTAL,
    ATTR_INPUT_3_VOLTAGE,
    ATTR_INPUT_3_AMPERAGE,
    ATTR_INPUT_3_POWER,
    ATTR_INPUT_3_ENERGY_TODAY,
    ATTR_INPUT_3_ENERGY_TOTAL,
    ATTR_INPUT_4_VOLTAGE,
    ATTR_INPUT_4_AMPERAGE,
    ATTR_INPUT_4_POWER,
    ATTR_INPUT_4_ENERGY_TODAY,
    ATTR_INPUT_4_ENERGY_TOTAL,
    ATTR_INPUT_5_VOLTAGE,
    ATTR_INPUT_5_AMPERAGE,
    ATTR_INPUT_5_POWER,
    ATTR_INPUT_5_ENERGY_TODAY,
    ATTR_INPUT_5_ENERGY_TOTAL,
    ATTR_INPUT_6_VOLTAGE,
    ATTR_INPUT_6_AMPERAGE,
    ATTR_INPUT_6_POWER,
    ATTR_INPUT_6_ENERGY_TODAY,
    ATTR_INPUT_6_ENERGY_TOTAL,
    ATTR_INPUT_7_VOLTAGE,
    ATTR_INPUT_7_AMPERAGE,
    ATTR_INPUT_7_POWER,
    ATTR_INPUT_7_ENERGY_TODAY,
    ATTR_INPUT_7_ENERGY_TOTAL,
    ATTR_INPUT_8_VOLTAGE,
    ATTR_INPUT_8_AMPERAGE,
    ATTR_INPUT_8_POWER,
    ATTR_INPUT_8_ENERGY_TODAY,
    ATTR_INPUT_8_ENERGY_TOTAL,
    ATTR_OUTPUT_POWER,
    ATTR_OUTPUT_ENERGY_TODAY,
    ATTR_OUTPUT_ENERGY_TOTAL,
    ATTR_OUTPUT_REACTIVE_POWER,
    ATTR_OUTPUT_REACTIVE_ENERGY_TODAY,
    ATTR_OUTPUT_REACTIVE_ENERGY_TOTAL,
    ATTR_OUTPUT_1_VOLTAGE,
    ATTR_OUTPUT_1_AMPERAGE,
    ATTR_OUTPUT_1_POWER,
    ATTR_OUTPUT_2_VOLTAGE,
    ATTR_OUTPUT_2_AMPERAGE,
    ATTR_OUTPUT_2_POWER,
    ATTR_OUTPUT_3_VOLTAGE,
    ATTR_OUTPUT_3_AMPERAGE,
    ATTR_OUTPUT_3_POWER,
    ATTR_OPERATION_HOURS,
    ATTR_FREQUENCY,
    ATTR_TEMPERATURE,
    ATTR_IPM_TEMPERATURE,
    ATTR_BOOST_TEMPERATURE,
    ATTR_P_BUS_VOLTAGE,
    ATTR_N_BUS_VOLTAGE,
    ATTR_OUTPUT_PERCENTAGE,
    ATTR_SOC_PERCENTAGE, ATTR_DISCHARGE_POWER, ATTR_CHARGE_POWER, ATTR_ENERGY_TO_USER_TODAY, ATTR_ENERGY_TO_USER_TOTAL,
    ATTR_ENERGY_TO_GRID_TODAY, ATTR_ENERGY_TO_GRID_TOTAL, ATTR_DISCHARGE_ENERGY_TODAY, ATTR_DISCHARGE_ENERGY_TOTAL,
    ATTR_CHARGE_ENERGY_TODAY, ATTR_CHARGE_ENERGY_TOTAL, ATTR_AC_CHARGE_ENABLED, ATTR_SERIAL_NUMBER, ATTR_TIME_1,
    ATTR_TIME_1_START, ATTR_TIME_1_END, ATTR_TIME_1_PRIORITY, ATTR_TIME_2, ATTR_TIME_3, ATTR_TIME_4, ATTR_TIME_5, ATTR_TIME_6,
)

MAXIMUM_DATA_LENGTH = 100
_LOGGER = logging.getLogger(__name__)


def model(registers) -> str:
    mo = (registers[0] << 16) + registers[1]
    return "A{:X} B{:X} D{:X} T{:X} P{:X} U{:X} M{:X} S{:X}".format(
        (mo & 0xF0000000) >> 28,
        (mo & 0x0F000000) >> 24,
        (mo & 0x00F00000) >> 20,
        (mo & 0x000F0000) >> 16,
        (mo & 0x0000F000) >> 12,
        (mo & 0x00000F00) >> 8,
        (mo & 0x000000F0) >> 4,
        (mo & 0x0000000F)
    )


def timeX(registers) -> str:
    start = timeX_start(registers[0])
    end = timeX_end(registers[1])

    dictionary = {
        'Start': datetime.time(start['Hour'], start['Minutes']).isoformat(timespec='minutes'),
        'End': datetime.time(end['Hour'], end['Minutes']).isoformat(timespec='minutes'),
        'Priority': start['Priority'],
        'Enabled': start['Enabled']
    }

    converted = str()

    # iterating over dictionary using a for loop
    for key in dictionary:
        converted += key + ": " + str(dictionary[key]) + ", "

    _LOGGER.debug("time: %s", converted)
    return converted


def timeX_start(registers) -> dict:
    bits = bin(registers)[2:].zfill(16)  # Convert to binary string, zero-padded to 16 bits
    minutes = int(bits[9:15], 2)
    hour = int(bits[4:8], 2)
    priority = int(bits[1:3], 2)
    enabled = int(bits[0], 2)
    priority_mapping = {
        0: 'Load',
        1: 'Battery',
        2: 'Grid'
    }
    enabled_mapping = {
        0: 'No',
        1: 'Yes'
    }
    dictionary = {
        'Minutes': minutes,
        'Hour': hour,
        'Priority': priority_mapping.get(priority, 'Unknown'),
        'Enabled': enabled_mapping.get(enabled, 'Unknown')
    }
    return dictionary


def timeX_end(registers) -> dict:
    bits = bin(registers)[2:].zfill(16)  # Convert to binary string, zero-padded to 16 bits
    minutes = int(bits[9:15], 2)
    hour = int(bits[3:8], 2)

    return {
        'Minutes': minutes,
        'Hour': hour
    }


def time_x_start(registers) -> str:
    bits = bin(registers)[2:].zfill(16)
    minutes = int(bits[9:15], 2)
    hour = int(bits[4:8], 2)

    return str(datetime.time(hour, minutes).isoformat(timespec='minutes'))


def time_x_enabled(registers) -> bool:
    bits = bin(registers)[2:].zfill(16)
    enabled = int(bits[0], 2)

    return enabled == 1


def time_x_priority(registers) -> str:
    bits = bin(registers)[2:].zfill(16)
    priority = int(bits[1:3], 2)
    priority_mapping = {
        0: 'Load',
        1: 'Battery',
        2: 'Grid'
    }

    return priority_mapping.get(priority, 'Unknown')


def time_x_end(registers) -> str:
    bits = bin(registers)[2:].zfill(16)
    minutes = int(bits[9:15], 2)
    hour = int(bits[3:8], 2)

    return str(datetime.time(hour, minutes).isoformat(timespec='minutes'))


SERIAL_NUMBER_REGISTER = GrowattDeviceRegisters(
    name=ATTR_SERIAL_NUMBER, register=3001, value_type=str, length=15
)

HOLDING_REGISTERS: tuple[GrowattDeviceRegisters, ...] = (
    FIRMWARE_REGISTER,
    SERIAL_NUMBER_REGISTER,
    GrowattDeviceRegisters(
        name=ATTR_INVERTER_MODEL,
        register=28,
        value_type=custom_function,
        length=2,
        function=model
    ),
    GrowattDeviceRegisters(
        name=ATTR_TIME_1,
        register=3038,
        value_type=custom_function,
        length=2,
        function=timeX
    ),
    GrowattDeviceRegisters(
        name=ATTR_TIME_1_START,
        register=3038,
        value_type=custom_function,
        length=1,
        function=time_x_start
    ),
    GrowattDeviceRegisters(
        name=ATTR_TIME_1_END,
        register=3039,
        value_type=custom_function,
        length=1,
        function=time_x_end
    ),
    GrowattDeviceRegisters(
        name=ATTR_TIME_1_PRIORITY,
        register=3038,
        value_type=custom_function,
        length=1,
        function=time_x_priority
    ),
    GrowattDeviceRegisters(
        name=ATTR_TIME_2,
        register=3040,
        value_type=custom_function,
        length=2,
        function=timeX
    ),
    GrowattDeviceRegisters(
        name=ATTR_TIME_3,
        register=3042,
        value_type=custom_function,
        length=2,
        function=timeX
    ),
    GrowattDeviceRegisters(
        name=ATTR_TIME_4,
        register=3044,
        value_type=custom_function,
        length=2,
        function=timeX
    ),
    DEVICE_TYPE_CODE_REGISTER,
    NUMBER_OF_TRACKERS_AND_PHASES_REGISTER,
    GrowattDeviceRegisters(
        name=ATTR_MODBUS_VERSION,
        register=88,
        value_type=float,
        scale=100
    ),
    GrowattDeviceRegisters(
        name=ATTR_AC_CHARGE_ENABLED,
        register=3049,
        value_type=int,
        length=1
    ),
)

INPUT_REGISTERS: tuple[GrowattDeviceRegisters, ...] = (
    GrowattDeviceRegisters(
        name=ATTR_STATUS_CODE, register=0, value_type=int
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_POWER, register=1, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_VOLTAGE, register=3, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_AMPERAGE, register=4, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_POWER, register=5, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_VOLTAGE, register=7, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_AMPERAGE, register=8, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_POWER, register=9, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_VOLTAGE, register=11, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_AMPERAGE, register=12, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_POWER, register=13, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_4_VOLTAGE, register=15, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_4_AMPERAGE, register=16, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_4_POWER, register=17, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_5_VOLTAGE, register=19, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_5_AMPERAGE, register=20, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_5_POWER, register=21, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_6_VOLTAGE, register=23, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_6_AMPERAGE, register=24, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_6_POWER, register=25, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_7_VOLTAGE, register=27, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_7_AMPERAGE, register=28, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_7_POWER, register=29, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_8_VOLTAGE, register=31, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_8_AMPERAGE, register=32, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_8_POWER, register=33, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_POWER, register=35, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_FREQUENCY, register=37, value_type=float, scale=100
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_1_VOLTAGE, register=38, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_1_AMPERAGE, register=39, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_1_POWER, register=40, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_2_VOLTAGE, register=42, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_2_AMPERAGE, register=43, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_2_POWER, register=44, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_3_VOLTAGE, register=46, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_3_AMPERAGE, register=47, value_type=float,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_3_POWER, register=48, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_ENERGY_TODAY, register=53, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_ENERGY_TOTAL, register=55, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OPERATION_HOURS, register=57, value_type=float, length=2, scale=7200,
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_ENERGY_TODAY, register=59, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_1_ENERGY_TOTAL, register=61, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_ENERGY_TODAY, register=63, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_2_ENERGY_TOTAL, register=65, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_ENERGY_TODAY, register=67, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_3_ENERGY_TOTAL, register=69, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_4_ENERGY_TODAY, register=71, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_4_ENERGY_TOTAL, register=73, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_5_ENERGY_TODAY, register=75, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_5_ENERGY_TOTAL, register=77, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_6_ENERGY_TODAY, register=79, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_6_ENERGY_TOTAL, register=81, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_7_ENERGY_TODAY, register=83, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_7_ENERGY_TOTAL, register=85, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_8_ENERGY_TODAY, register=87, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_8_ENERGY_TOTAL, register=89, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_INPUT_ENERGY_TOTAL, register=91, value_type=float, length=2
    ),
    GrowattDeviceRegisters(name=ATTR_TEMPERATURE, register=93, value_type=float),
    GrowattDeviceRegisters(name=ATTR_IPM_TEMPERATURE, register=94, value_type=float),
    GrowattDeviceRegisters(name=ATTR_BOOST_TEMPERATURE, register=95, value_type=float),
    GrowattDeviceRegisters(name=ATTR_P_BUS_VOLTAGE, register=98, value_type=float),
    GrowattDeviceRegisters(name=ATTR_N_BUS_VOLTAGE, register=99, value_type=float),
    GrowattDeviceRegisters(name=ATTR_OUTPUT_PERCENTAGE, register=101, value_type=int),
    GrowattDeviceRegisters(name=ATTR_DERATING_MODE, register=104, value_type=int),
    GrowattDeviceRegisters(name=ATTR_FAULT_CODE, register=105, value_type=int),
    GrowattDeviceRegisters(
        name=ATTR_WARNING_CODE, register=110, value_type=int, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_REACTIVE_POWER, register=58, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_REACTIVE_ENERGY_TODAY, register=60, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(
        name=ATTR_OUTPUT_REACTIVE_ENERGY_TOTAL, register=62, value_type=float, length=2,
    ),
    GrowattDeviceRegisters(name=ATTR_WARNING_VALUE, register=65, value_type=int),
    GrowattDeviceRegisters(
        name=ATTR_SOC_PERCENTAGE, register=3171, value_type=int
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_POWER, register=3178, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_POWER, register=3180, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_USER_TODAY, register=3067, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_USER_TOTAL, register=3069, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_GRID_TODAY, register=3071, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_ENERGY_TO_GRID_TOTAL, register=3073, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_ENERGY_TODAY, register=3125, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_DISCHARGE_ENERGY_TOTAL, register=3127, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_ENERGY_TODAY, register=3129, value_type=float, length=2
    ),
    GrowattDeviceRegisters(
        name=ATTR_CHARGE_ENERGY_TOTAL, register=3131, value_type=float, length=2
    ),
)
