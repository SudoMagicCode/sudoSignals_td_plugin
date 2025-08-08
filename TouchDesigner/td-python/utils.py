from datetime import datetime
import SudoSignals
from entityReference import entityReference


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


def Get_log_timeStamp() -> str:
    return datetime.now().isoformat(' ', 'seconds')


def Text_port_msg(level: str, msg: str) -> str:
    return f'{Get_log_timeStamp()} [*] SUDOSIGNALS :: {level} :: {msg}'


def entity_reference_from_parGroup(parGroup) -> dict[str, str]:
    entity_reference = entityReference.from_parGroup(parGroup=parGroup)
    return entity_reference.to_dict


def construct_signals_float(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.FLOAT,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.min],
        maxVal=[each for each in parGroup.max],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(parGroup=parGroup),
        readOnly=parGroup.readOnly,
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_color(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.COLOR,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.min],
        maxVal=[each for each in parGroup.max],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(parGroup=parGroup),
        readOnly=parGroup.readOnly,
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_int(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.INT,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.min],
        maxVal=[each for each in parGroup.max],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(parGroup=parGroup),
        readOnly=parGroup.readOnly,
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_toggle(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.TOGGLE,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.min],
        maxVal=[each for each in parGroup.max],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(parGroup=parGroup),
        readOnly=parGroup.readOnly,
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_pulse(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.PULSE,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.min],
        maxVal=[each for each in parGroup.max],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(parGroup=parGroup),
        readOnly=parGroup.readOnly,
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_string(parGroup) -> SudoSignals.signalsStr:
    new_control = SudoSignals.signalsStr(
        controlType=SudoSignals.signalsControlType.STR,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(parGroup=parGroup),
        readOnly=parGroup.readOnly,
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_header(parGroup) -> SudoSignals.signalsStr:
    new_control = SudoSignals.signalsStr(
        controlType=SudoSignals.signalsControlType.HEADER,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(parGroup=parGroup),
        readOnly=parGroup.readOnly,
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_menu(parGroup) -> SudoSignals.signalsMenu:
    current = parGroup[0]
    menuOptions = {}

    for index, each in enumerate(current.menuLabels):
        menuOptions[each] = current.menuNames[index]

    new_control = SudoSignals.signalsMenu(
        controlType=SudoSignals.signalsControlType.MENU,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        menuOptions=menuOptions,
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(parGroup=parGroup),
        readOnly=parGroup.readOnly,
        values=[each for each in parGroup.val]
    )
    return new_control


def control_not_yet_supported(parGroup):
    print(f'{parGroup.style} not yet supported by signals')


PAR_CONTROL_MAP = {
    'Float': construct_signals_float,
    'Int': construct_signals_int,
    'Str': construct_signals_string,
    'Menu': construct_signals_menu,
    'Toggle': construct_signals_toggle,
    'Momentary': construct_signals_pulse,
    'Pulse': construct_signals_pulse,
    'Header': construct_signals_header,
    'RGB': construct_signals_color,
    'RGBA': construct_signals_color,
    'UV': construct_signals_float,
    'UVW': construct_signals_float,
    'XY': construct_signals_float,
    'XYZ': construct_signals_float,
    'WH': construct_signals_int
}


def control_from_par_group(parGroup) -> SudoSignals.signalsControl:

    try:
        func = PAR_CONTROL_MAP.get(parGroup.style)
        new_control = func(parGroup)
        return new_control

    except Exception as e:
        print(f"{parGroup.label} failed")
        print(e)


def validate_action_name(actionType: str) -> bool:
    if actionType in SudoSignals.signalsActionType._member_names_:
        return True
    else:
        return False
