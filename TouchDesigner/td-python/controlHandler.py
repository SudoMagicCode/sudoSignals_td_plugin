from datetime import datetime
from entityReference import entityReference
import SudoSignals


def entity_reference_from_parGroup(parGroup) -> dict[str, str]:
    entity_reference = entityReference.from_parGroup(parGroup=parGroup)
    return entity_reference.to_dict


def construct_signals_float(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.FLOAT,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.normMin],
        maxVal=[each for each in parGroup.normMax],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(
            parGroup=parGroup),
        # a par can only be read only or not, partial not currently supported
        readOnly=any(parGroup.readOnly),
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_color(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.COLOR,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.normMin],
        maxVal=[each for each in parGroup.normMax],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(
            parGroup=parGroup),
        # a par can only be read only or not, partial not currently supported
        readOnly=any(parGroup.readOnly),
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_int(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.INT,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.normMin],
        maxVal=[each for each in parGroup.normMax],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(
            parGroup=parGroup),
        # a par can only be read only or not, partial not currently supported
        readOnly=any(parGroup.readOnly),
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_toggle(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.TOGGLE,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.normMin],
        maxVal=[each for each in parGroup.normMax],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(
            parGroup=parGroup),
        # a par can only be read only or not, partial not currently supported
        readOnly=any(parGroup.readOnly),
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_pulse(parGroup) -> SudoSignals.signalsNumber:
    new_control = SudoSignals.signalsNumber(
        controlType=SudoSignals.signalsControlType.PULSE,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        minVal=[each for each in parGroup.normMin],
        maxVal=[each for each in parGroup.normMax],
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(
            parGroup=parGroup),
        # a par can only be read only or not, partial not currently supported
        readOnly=any(parGroup.readOnly),
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
        entityReference=entity_reference_from_parGroup(
            parGroup=parGroup),
        # a par can only be read only or not, partial not currently supported
        readOnly=any(parGroup.readOnly),
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
        entityReference=entity_reference_from_parGroup(
            parGroup=parGroup),
        # a par can only be read only or not, partial not currently supported
        readOnly=any(parGroup.readOnly),
        values=[each for each in parGroup.val]
    )
    return new_control


def construct_signals_menu(parGroup) -> SudoSignals.signalsMenu:
    current = parGroup[0]
    menuOptions = {}

    for index, each in enumerate(current.menuNames):
        menuOptions[each] = current.menuLabels[index]

    new_control = SudoSignals.signalsMenu(
        controlType=SudoSignals.signalsControlType.MENU,
        index=parGroup.order,
        defaultValues=[each for each in parGroup.default],
        label=parGroup.label,
        menuOptions=menuOptions,
        path=f'{parGroup.owner.path}#{parGroup.label}',
        entityReference=entity_reference_from_parGroup(
            parGroup=parGroup),
        # a par can only be read only or not, partial not currently supported
        readOnly=any(parGroup.readOnly),
        values=[each for each in parGroup.val]
    )
    return new_control


def control_not_yet_supported(parGroup):
    print(f'{parGroup.style} not yet supported by signals')
