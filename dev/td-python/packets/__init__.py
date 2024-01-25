
try:
	import corePackets_pb2
	import dataTypes_pb2
except:
	print("[~] WARNING! Could not import protobuf types. Please add them to the python path.")


def CreateIdentifyPacket(software, softwareVersion, pluginVersion):
	newPacket = corePackets_pb2.CorePacket()
	newPacket.action = corePackets_pb2.PacketType.IDENTIFY
	newLocalIdentifier = corePackets_pb2.LocalIdentifier()
	newLocalIdentifier.processId = "7890"
	newPacket.local.CopyFrom(newLocalIdentifier)
	newIdentifyData = dataTypes_pb2.IdentifyData()
	newIdentifyData.software = software
	newIdentifyData.version = softwareVersion
	newPacket.data.Pack(newIdentifyData)

	return newPacket 