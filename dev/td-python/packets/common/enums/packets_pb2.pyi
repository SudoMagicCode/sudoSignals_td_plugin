from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PacketOriginationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORIGINATION_UNKNOWN: _ClassVar[PacketOriginationType]
    SERVICES: _ClassVar[PacketOriginationType]
    MACHINE_DIRECT: _ClassVar[PacketOriginationType]
    MACHINE_PROXY: _ClassVar[PacketOriginationType]
    PROCESS: _ClassVar[PacketOriginationType]
    DASHBOARD: _ClassVar[PacketOriginationType]
    API: _ClassVar[PacketOriginationType]
    UNKNOWN: _ClassVar[PacketOriginationType]

class PacketType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PACKET_TYPE_UNKNOWN: _ClassVar[PacketType]
    ACKNOWLEDGED: _ClassVar[PacketType]
    START: _ClassVar[PacketType]
    INFO: _ClassVar[PacketType]
    END: _ClassVar[PacketType]
    CREATE_ACCESS: _ClassVar[PacketType]
    CREATE_SOURCE: _ClassVar[PacketType]
    CREATE_SUBSCRIBER: _ClassVar[PacketType]
    ACCESS_UPDATE: _ClassVar[PacketType]
    SOURCE_UPDATE: _ClassVar[PacketType]
    SUBSCRIBER_UPDATE: _ClassVar[PacketType]
    SUBSCRIBER_DELETE: _ClassVar[PacketType]
    MACHINE_LOG: _ClassVar[PacketType]
    MACHINE_REPORT: _ClassVar[PacketType]
    MACHINE_CONTROLS: _ClassVar[PacketType]
    MACHINE_INFO: _ClassVar[PacketType]
    MACHINE_UPDATE: _ClassVar[PacketType]
    PROCESS_IDENTIFY: _ClassVar[PacketType]
    PROCESS_LOG: _ClassVar[PacketType]
    PROCESS_REPORT: _ClassVar[PacketType]
    PROCESS_CONTROLS: _ClassVar[PacketType]
    SUBSCRIPTION_CREATE: _ClassVar[PacketType]
    SUBSCRIPTION_PARTIAL: _ClassVar[PacketType]
    SUBSCRIPTION_DATA: _ClassVar[PacketType]
    ACCESS_INFO: _ClassVar[PacketType]
    RTC_SIGNALING: _ClassVar[PacketType]
    PROFILE_CREATE: _ClassVar[PacketType]
    PROFILE_UPDATE: _ClassVar[PacketType]
    PROFILE_DELETE: _ClassVar[PacketType]
    PROFILE_SET_ACTIVE: _ClassVar[PacketType]
    PROFILE_INFO: _ClassVar[PacketType]
    SOURCE_LOG: _ClassVar[PacketType]
    SOURCE_REPORT: _ClassVar[PacketType]
    SOURCE_CONTROLS: _ClassVar[PacketType]
    SOURCE_INFO: _ClassVar[PacketType]

class SignalingPacketType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GATHER: _ClassVar[SignalingPacketType]
    ACTIVE_OFFERS: _ClassVar[SignalingPacketType]
    OFFER: _ClassVar[SignalingPacketType]
    ANSWER: _ClassVar[SignalingPacketType]
    ICE_CANDIDATE: _ClassVar[SignalingPacketType]
ORIGINATION_UNKNOWN: PacketOriginationType
SERVICES: PacketOriginationType
MACHINE_DIRECT: PacketOriginationType
MACHINE_PROXY: PacketOriginationType
PROCESS: PacketOriginationType
DASHBOARD: PacketOriginationType
API: PacketOriginationType
UNKNOWN: PacketOriginationType
PACKET_TYPE_UNKNOWN: PacketType
ACKNOWLEDGED: PacketType
START: PacketType
INFO: PacketType
END: PacketType
CREATE_ACCESS: PacketType
CREATE_SOURCE: PacketType
CREATE_SUBSCRIBER: PacketType
ACCESS_UPDATE: PacketType
SOURCE_UPDATE: PacketType
SUBSCRIBER_UPDATE: PacketType
SUBSCRIBER_DELETE: PacketType
MACHINE_LOG: PacketType
MACHINE_REPORT: PacketType
MACHINE_CONTROLS: PacketType
MACHINE_INFO: PacketType
MACHINE_UPDATE: PacketType
PROCESS_IDENTIFY: PacketType
PROCESS_LOG: PacketType
PROCESS_REPORT: PacketType
PROCESS_CONTROLS: PacketType
SUBSCRIPTION_CREATE: PacketType
SUBSCRIPTION_PARTIAL: PacketType
SUBSCRIPTION_DATA: PacketType
ACCESS_INFO: PacketType
RTC_SIGNALING: PacketType
PROFILE_CREATE: PacketType
PROFILE_UPDATE: PacketType
PROFILE_DELETE: PacketType
PROFILE_SET_ACTIVE: PacketType
PROFILE_INFO: PacketType
SOURCE_LOG: PacketType
SOURCE_REPORT: PacketType
SOURCE_CONTROLS: PacketType
SOURCE_INFO: PacketType
GATHER: SignalingPacketType
ACTIVE_OFFERS: SignalingPacketType
OFFER: SignalingPacketType
ANSWER: SignalingPacketType
ICE_CANDIDATE: SignalingPacketType
