from datetime import datetime
from google.protobuf import struct_pb2
import packets
import parGroupFuncs
import helperTypes

styleToControlTypeMap = {
    "Float": packets.signalsEnums_pb2.ControlType.CONTROL_FLOAT,
    "Int": packets.signalsEnums_pb2.ControlType.CONTROL_INT,
    "Header": packets.signalsEnums_pb2.ControlType.CONTROL_HEADER,
    "Str": packets.signalsEnums_pb2.ControlType.CONTROL_STRING,
    "Pulse": packets.signalsEnums_pb2.ControlType.CONTROL_PULSE,
    "Toggle": packets.signalsEnums_pb2.ControlType.CONTROL_TOGGLE,
    "Menu": packets.signalsEnums_pb2.ControlType.CONTROL_MENU,
    "StrMenu": packets.signalsEnums_pb2.ControlType.CONTROL_MENU,
    "RGB": packets.signalsEnums_pb2.ControlType.CONTROL_FLOAT,
    "RGBA": packets.signalsEnums_pb2.ControlType.CONTROL_FLOAT,
    "UV": packets.signalsEnums_pb2.ControlType.CONTROL_FLOAT,
    "UVW": packets.signalsEnums_pb2.ControlType.CONTROL_FLOAT,
    "XY": packets.signalsEnums_pb2.ControlType.CONTROL_FLOAT,
    "XYZ": packets.signalsEnums_pb2.ControlType.CONTROL_FLOAT,
    "WH": packets.signalsEnums_pb2.ControlType.CONTROL_FLOAT,
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
    'RGB': parGroupFuncs.parGroupFloatFunc,
    'RGBA': parGroupFuncs.parGroupFloatFunc,
    'UV': parGroupFuncs.parGroupFloatFunc,
    'UVW': parGroupFuncs.parGroupFloatFunc,
    'XY': parGroupFuncs.parGroupFloatFunc,
    'XYZ': parGroupFuncs.parGroupFloatFunc,
    'WH': parGroupFuncs.parGroupFloatFunc,
    'Toggle': parGroupFuncs.parGroupToggleFunc
}


def parDataBlock(parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # construct new control
    newControl = packets.fieldTypes_pb2.Control()

    newControl.controlType = styleToControlTypeMap[parGroup.style]
    newControl.label = parGroup.label
    newControl.entityReference["path"] = parGroup.owner.path
    newControl.entityReference["name"] = parGroup.name
    newControl.index = parGroup.order

    # use parGroup funcs to match to an appropriate function and fill in control
    parGroupFunc = parGroupFunctionMap.get(parGroup.style)
    if parGroupFunc != None:
        control = parGroupFunc(newControl, parGroup)
    else:
        control = newControl

    return control


def groupDataBlock(group) -> packets.fieldTypes_pb2.Control:
    return parDataBlock(group)


def CreateAllParDataBlocks(page) -> dict[str, packets.fieldTypes_pb2.Control]:
    parsData = {}
    groups = page.parGroups
    for g in groups:
        parsData[g.name] = groupDataBlock(g)
    return parsData


def GetLogTimeStamp() -> str:
    return datetime.now().isoformat(' ', 'seconds')


def TextPortMsg(level: str, msg: str) -> str:
    return f'{GetLogTimeStamp()} [*] SUDOSIGNALS :: {level} :: {msg}'
