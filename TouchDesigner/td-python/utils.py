from datetime import datetime
from google.protobuf import struct_pb2
import packets
import parGroupFuncs
import helperTypes

styleToControlTypeMap = {
    "Float": packets.control_enums.CONTROL_FLOAT,
    "Int": packets.control_enums.CONTROL_INT,
    "Header": packets.control_enums.CONTROL_HEADER,
    "Str": packets.control_enums.CONTROL_STRING,
    "Pulse": packets.control_enums.CONTROL_PULSE,
    "Toggle": packets.control_enums.CONTROL_TOGGLE,
    "Menu": packets.control_enums.CONTROL_MENU,
    "StrMenu": packets.control_enums.CONTROL_MENU,
    "RGB": packets.control_enums.CONTROL_COLOR,
    "RGBA": packets.control_enums.CONTROL_COLOR,
    "UV": packets.control_enums.CONTROL_FLOAT,
    "UVW": packets.control_enums.CONTROL_FLOAT,
    "XY": packets.control_enums.CONTROL_FLOAT,
    "XYZ": packets.control_enums.CONTROL_FLOAT,
    "WH": packets.control_enums.CONTROL_FLOAT,
}

parGroupFunctionMap = {
    'Float': parGroupFuncs.parGroupFloatFunc,
    'Int': parGroupFuncs.parGroupIntFunc,
    'Menu': parGroupFuncs.parGroupMenuFunc,
    'StrMenu': parGroupFuncs.parGroupMenuFunc,
    'Momentary': parGroupFuncs.parGroupMomentaryFunc,
    'Header': parGroupFuncs.parGroupHeaderFunc,
    'Pulse': parGroupFuncs.parGroupPulseFunc,
    'Python': parGroupFuncs.parGroupPythonFunc,
    'Sequence': parGroupFuncs.parGroupSequenceFunc,
    'Str': parGroupFuncs.parGroupStringFunc,
    'RGB': parGroupFuncs.parGroupRGBFunc,
    'RGBA': parGroupFuncs.parGroupRGBAFunc,
    'UV': parGroupFuncs.parGroupFloatFunc,
    'UVW': parGroupFuncs.parGroupFloatFunc,
    'XY': parGroupFuncs.parGroupFloatFunc,
    'XYZ': parGroupFuncs.parGroupFloatFunc,
    'WH': parGroupFuncs.parGroupFloatFunc,
    'Toggle': parGroupFuncs.parGroupToggleFunc
}


def parDataBlock(parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # construct new control
    newControl = packets.controls.Control()

    newControl.control_type = styleToControlTypeMap[parGroup.style]
    newControl.label.CopyFrom(packets.controls_fields.ControlLabel(value=parGroup.label))
    newControl.entity_reference.value["path"] = parGroup.owner.path
    newControl.entity_reference.value["name"] = parGroup.name
    newControl.index.CopyFrom(packets.controls_fields.ControlIndex(value=parGroup.order))

    # use parGroup funcs to match to an appropriate function and fill in control
    parGroupFunc = parGroupFunctionMap.get(parGroup.style)
    if parGroupFunc != None:
        control = parGroupFunc(newControl, parGroup)
    else:
        control = newControl

    return control


def groupDataBlock(group) -> packets.controls.Control:
    return parDataBlock(group)


def CreateAllParDataBlocks(page) -> dict[str, packets.controls.Control]:
    parsData = {}
    groups = page.parGroups
    for g in groups:
        parsData[g.name] = groupDataBlock(g)
    return parsData


def GetLogTimeStamp() -> str:
    return datetime.now().isoformat(' ', 'seconds')


def TextPortMsg(level: str, msg: str) -> str:
    return f'{GetLogTimeStamp()} [*] SUDOSIGNALS :: {level} :: {msg}'
