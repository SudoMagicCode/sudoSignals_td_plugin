import common.fieldTypes_pb2 as fieldTypes_pb2
import common.packets_pb2 as packets_pb2
import common.payloads_pb2 as payloads_pb2
import common.signalsEnums_pb2 as signalsEnums_pb2
import common.signalsOptions_pb2 as signalsOptions_pb2
from objects import *


def CreateIdentifyPacket(signals_id, software, softwareVersion, pluginVersion):
    newPacket = packets_pb2.WebsocketPacket()
    newPacket.action = packets_pb2.WebsocketPacket.PROCESS_IDENTIFY

    newIdentity = packets_pb2.PacketIdentity()
    newIdentity.origin = packets_pb2.PacketIdentity.PROCESS
    newIdentity.additionalIdentifiers['process_id'] = signals_id
    newIdentity.additionalIdentifiers['software'] = software
    newIdentity.additionalIdentifiers['software_version'] = softwareVersion
    newIdentity.additionalIdentifiers['plugin_version'] = pluginVersion
    newPacket.identity.CopyFrom(newIdentity)
    return newPacket


def CreateLogPacket(logLevel: signalsEnums_pb2.LogLevel, message: str):
    newPacket = packets_pb2.WebsocketPacket()
    newPacket.action = packets_pb2.WebsocketPacket.PROCESS_LOG

    newIdentity = packets_pb2.PacketIdentity()
    newIdentity.origin = packets_pb2.PacketIdentity.PROCESS

    newLogPayload = fieldTypes_pb2.Log()
    newLogPayload.level = logLevel
    newLogPayload.message = message

    newPacket.payload.Pack(newLogPayload)

    return newPacket


def CreateReportPacket(dataFrame: fieldTypes_pb2.DataFrame):
    newPacket = packets_pb2.WebsocketPacket()
    newPacket.action = packets_pb2.WebsocketPacket.PROCESS_REPORT

    newIdentity = packets_pb2.PacketIdentity()
    newIdentity.origin = packets_pb2.PacketIdentity.PROCESS

    newReportPayload = fieldTypes_pb2.Report()
    newReportPayload.data.CopyFrom(dataFrame)

    newPacket.payload.Pack(newReportPayload)

    return newPacket


def CreateControlPacket(controlData: list[fieldTypes_pb2.ControlPage]):
    newPacket = packets_pb2.WebsocketPacket()
    newPacket.action = packets_pb2.WebsocketPacket.PROCESS_CONTROLS

    newIdentity = packets_pb2.PacketIdentity()
    newIdentity.origin = packets_pb2.PacketIdentity.PROCESS

    newControlPayload = payloads_pb2.ProcessControlPayload()

    for controlPage in controlData:

        newControlPayload.data[controlPage.uuid].CopyFrom(controlPage)

    newPacket.payload.Pack(newControlPayload)

    return newPacket
