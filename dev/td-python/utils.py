from datetime import datetime
import packets
from google.protobuf import struct_pb2



styleToControlTypeMap = {
	"Float": packets.signalsEnums_pb2.ControlType.CONTROL_FLOAT,
	"Int": packets.signalsEnums_pb2.ControlType.CONTROL_INT,
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



def parDataBlock(parGroup) -> packets.fieldTypes_pb2.Control:
	newControl = packets.fieldTypes_pb2.Control()

	newControl.controlType = styleToControlTypeMap[parGroup.style]
	newControl.label = parGroup.label
	newControl.entityReference["path"] = parGroup.owner.path
	newControl.entityReference["name"] = parGroup.name
	newControl.index = parGroup.index

	for index, parVal in enumerate(parGroup.val):
		if parVal is not None:
			newValue = struct_pb2.Value()
			newMin = struct_pb2.Value()
			newMax = struct_pb2.Value()
			newDefault = struct_pb2.Value()
			if isinstance(parVal, str):
				newValue.string_value = parVal
				newDefault.string_value = parGroup.default[index]
			elif isinstance(parVal, int | float):
				newValue.number_value = parVal
				newMin.number_value = parGroup.min[index]
				newMax.number_value = parGroup.max[index]
				newDefault.number_value = parGroup.default[index]
				newControl.minVal.append(newMin)
				newControl.maxVal.append(newMax)
			elif isinstance(parVal, bool):
				newValue.bool_value = parVal	
				newDefault.bool_value = parGroup.default[index]
			
			newControl.values.append(newValue)
			newControl.defaultValues.append(newDefault)
	return newControl
	
def groupDataBlock(group) -> packets.fieldTypes_pb2.Control:
	return parDataBlock(group)

def CreateAllParDataBlocks(page) -> dict[str, packets.fieldTypes_pb2.Control] :
	parsData = {}
	groups = page.parGroups
	for g in groups:
		parsData[g.name] = groupDataBlock(g)
	return parsData

def GetLogTimeStamp() -> str:
	return datetime.now().isoformat(' ', 'seconds')

def TextPortMsg(level:str, msg:str) -> str:
	return f'{GetLogTimeStamp()} [*] SUDOSIGNALS :: {level} :: {msg}'