try:
	import corePackets_pb2
	import dataTypes_pb2
	import packets_pb2
	import signalsOptions_pb2
	import sudoSignalsTypes_pb2
	import dynamo_pb2
	import fieldTypes_pb2
	import payloads_pb2
	import records_pb2
except:
	print("[~] WARNING! Could not import protobuf types. Please add them to the python path.")


def CreateIdentifyPacket(signals_id, software, softwareVersion, pluginVersion):
	newPacket = corePackets_pb2.CorePacket()
	newPacket.action = corePackets_pb2.PacketType.IDENTIFY
	newLocalIdentifier = corePackets_pb2.LocalIdentifier()
	newLocalIdentifier.processId = signals_id
	newPacket.local.CopyFrom(newLocalIdentifier)
	newIdentifyData = dataTypes_pb2.IdentifyData()
	newIdentifyData.software = software
	newIdentifyData.version = softwareVersion
	newPacket.data.Pack(newIdentifyData)

	return newPacket 