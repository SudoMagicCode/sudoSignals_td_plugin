from datetime import datetime
import controlHandler
import SudoSignals


LINKS: dict[str, str] = {
    'Help': "https://sudomagiccode.github.io/SudoSignals/",
    'Forum': "https://github.com/SudoMagicCode/SudoSignals/discussions",
    'Sudosignalsdashboard': "https://dashboard.sudosignals.com/",
    'Bugreport': "https://forms.clickup.com/f/16ky7-1036/3TNCU1Q2JMMEZ5XS43"
}

RELEASE_SOURCE: str = "https://github.com/SudoMagicCode/sudoSignals_td_plugin_releases/releases/latest"

VALID_LOG_LEVELS: list[int] = [0, 1, 2, 3, 4]

LOG_MAP_LOOKUP: dict['str', 'int'] = {
    "LOG": 0,
    "INFO": 1,
    "WARN": 2,
    "CRIT": 3,
    "ALERT": 4
}

LOG_LEVEL_LOOKUP: dict['str': SudoSignals.signalsLogLevel] = {
    '0': SudoSignals.signalsLogLevel.LOG,
    '1': SudoSignals.signalsLogLevel.INFO,
    '2': SudoSignals.signalsLogLevel.WARN,
    '3': SudoSignals.signalsLogLevel.CRIT,
    '4': SudoSignals.signalsLogLevel.ALERT
}

CONTROL_TYPE_MAP = {
    SudoSignals.signalsControlType.FLOAT: SudoSignals.signalsNumber,
    SudoSignals.signalsControlType.INT: SudoSignals.signalsNumber,
    SudoSignals.signalsControlType.MENU: SudoSignals.signalsMenu,
    SudoSignals.signalsControlType.PULSE: SudoSignals.signalsNumber,
    SudoSignals.signalsControlType.STR: SudoSignals.signalsStr,
    SudoSignals.signalsControlType.TOGGLE: SudoSignals.signalsNumber,
    SudoSignals.signalsControlType.HEADER: SudoSignals.signalsStr,
    SudoSignals.signalsControlType.COLOR: SudoSignals.signalsNumber,
}

PAR_CONTROL_MAP = {
    'Float': controlHandler.construct_signals_float,
    'Int': controlHandler.construct_signals_int,
    'Str': controlHandler.construct_signals_string,
    'Menu': controlHandler.construct_signals_menu,
    'Toggle': controlHandler.construct_signals_toggle,
    'Momentary': controlHandler.construct_signals_pulse,
    'Pulse': controlHandler.construct_signals_pulse,
    'Header': controlHandler.construct_signals_header,
    'RGB': controlHandler.construct_signals_color,
    'RGBA': controlHandler.construct_signals_color,
    'UV': controlHandler.construct_signals_float,
    'UVW': controlHandler.construct_signals_float,
    'XY': controlHandler.construct_signals_float,
    'XYZ': controlHandler.construct_signals_float,
    'WH': controlHandler.construct_signals_int
}


def Get_log_timeStamp() -> str:
    return datetime.now().isoformat(' ', 'seconds')


def Text_port_msg(level: str, msg: str) -> str:
    return f'{Get_log_timeStamp()} [*] SUDOSIGNALS :: {level} :: {msg}'


def control_from_par_group(parGroup) -> SudoSignals.signalsControl:
    try:
        func = PAR_CONTROL_MAP.get(parGroup.style)
        new_control: SudoSignals.signalsControl = func(parGroup)
        return new_control

    except Exception as e:
        print(f"{parGroup.label} failed")
        print(e)


def control_from_dict(data: dict) -> SudoSignals.signalsControl:
    control_type = SudoSignals.signalsControlType(data.get('controlType'))
    try:
        func = CONTROL_TYPE_MAP.get(control_type)
        new_control = func.from_dict(data)
        return new_control

    except Exception as e:
        print(f'failed to construct control for {control_type.value}')
        print(e)


def validate_action_name(actionType: str) -> bool:
    action = SudoSignals.signalsActionType(actionType)
    if action in SudoSignals.signalsActionType:
        return True
    else:
        return False
