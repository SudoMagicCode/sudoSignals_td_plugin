from datetime import datetime
import packets
from google.protobuf import struct_pb2



styleToControlTypeMap = {
	"Float": packets.fieldTypes_pb2.Control.ControlType.FLOAT,
	"Int": packets.fieldTypes_pb2.Control.ControlType.INT,
	"Str": packets.fieldTypes_pb2.Control.ControlType.STRING,
	"Pulse": packets.fieldTypes_pb2.Control.ControlType.PULSE,
	"Toggle": packets.fieldTypes_pb2.Control.ControlType.TOGGLE,
	"Menu": packets.fieldTypes_pb2.Control.ControlType.MENU,
	"StrMenu": packets.fieldTypes_pb2.Control.ControlType.MENU,
	"RGB": packets.fieldTypes_pb2.Control.ControlType.FLOAT,
	"RGBA": packets.fieldTypes_pb2.Control.ControlType.FLOAT,
	"UV": packets.fieldTypes_pb2.Control.ControlType.FLOAT,
	"UVW": packets.fieldTypes_pb2.Control.ControlType.FLOAT,
	"XY": packets.fieldTypes_pb2.Control.ControlType.FLOAT,
	"XYZ": packets.fieldTypes_pb2.Control.ControlType.FLOAT,
	"WH": packets.fieldTypes_pb2.Control.ControlType.FLOAT,
}



def parDataBlock(parGroup) -> packets.fieldTypes_pb2.Control:
	newControl = packets.fieldTypes_pb2.Control()

	newControl.controlType = styleToControlTypeMap[parGroup.style]
	newControl.label = parGroup.label
	newControl.entityReference["path"] = parGroup.owner.path
	newControl.entityReference["name"] = parGroup.name

	for parVal in parGroup.val:
		if parVal is not None:
			newValue = struct_pb2.Value()
			if isinstance(parVal, str):
				newValue.string_value = parVal
			elif isinstance(parVal, int | float):
				newValue.number_value = parVal
			elif isinstance(parVal, bool):
				newValue.bool_value = parVal	
			
			newControl.values.append(newValue)
	return newControl
	
def groupDataBlock(group) -> packets.fieldTypes_pb2.Control:
	return parDataBlock(group)

def CreateAllParDataBlocks(page) -> dict[int, packets.fieldTypes_pb2.Control] :
	parsData = {}
	groups = page.parGroups
	for idx,g in enumerate(groups):
		parsData[idx] = groupDataBlock(g)
	return parsData

def GetLogTimeStamp() -> str:
	return datetime.now().isoformat(' ', 'seconds')

def TextPortMsg(level:str, msg:str) -> str:
	return f'{GetLogTimeStamp()} [*] SUDOSIGNALS :: {level} :: {msg}'