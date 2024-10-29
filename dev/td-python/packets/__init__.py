
import common.generic_pb2 as generic
import common.enums.logs_pb2 as log_enums
import common.enums.packets_pb2 as packet_enums
import common.enums.data_field_pb2 as report_enums
import common.enums.controls_pb2 as control_enums

import common.packets.websockets_pb2 as websockets_packets
import common.payloads.process_pb2 as process_payloads
import objects.controls.controls_fields_pb2 as controls_fields
import objects.controls.controls_pb2 as controls
import objects.log.log_pb2 as logs
import objects.report.report_fields_pb2 as report_fields
import objects.report.report_pb2 as reports


def CreateIdentifyPacket(signals_id, software, softwareVersion, pluginVersion):
    newPacket = websockets_packets.WebsocketPacket()
    newPacket.action = packet_enums.PROCESS_IDENTIFY

    newIdentity = websockets_packets.PacketIdentity()
    newIdentity.origin = packet_enums.PROCESS
    newIdentity.additionalIdentifiers['process_id'] = signals_id
    newIdentity.additionalIdentifiers['software'] = software
    newIdentity.additionalIdentifiers['software_version'] = softwareVersion
    newIdentity.additionalIdentifiers['plugin_version'] = pluginVersion
    newPacket.identity.CopyFrom(newIdentity)
    return newPacket


def CreateLogPacket(logLevel: log_enums.LogLevel, message: str):
    newPacket = websockets_packets.WebsocketPacket()
    newPacket.action = packet_enums.PROCESS_LOG

    newIdentity = websockets_packets.PacketIdentity()
    newIdentity.origin = packet_enums.PROCESS

    newLogPayload = logs.Log()
    newLogPayload.level = logLevel
    newLogPayload.message = message

    newPacket.payload.Pack(newLogPayload)

    return newPacket


def CreateReportPacket(dataFrame: report_fields.DataFrame):
    newPacket = websockets_packets.WebsocketPacket()
    newPacket.action = packet_enums.PROCESS_REPORT

    newIdentity = websockets_packets.PacketIdentity()
    newIdentity.origin = packet_enums.PROCESS

    newReportPayload = reports.Report()
    newReportPayload.data.CopyFrom(dataFrame)

    newPacket.payload.Pack(newReportPayload)

    return newPacket


def CreateControlPacket(controlData: list[controls.ControlPage]):
    newPacket = websockets_packets.WebsocketPacket()
    newPacket.action = packet_enums.PROCESS_CONTROLS

    newIdentity = websockets_packets.PacketIdentity()
    newIdentity.origin = packet_enums.PROCESS

    newControlPayload = process_payloads.ProcessControlPayload()

    for controlPage in controlData:

        newControlPayload.data[controlPage.uuid.value].CopyFrom(controlPage)

    newPacket.payload.Pack(newControlPayload)

    return newPacket
