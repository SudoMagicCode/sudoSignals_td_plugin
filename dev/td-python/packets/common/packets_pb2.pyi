from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignalingPacketType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GATHER: _ClassVar[SignalingPacketType]
    ACTIVE_OFFERS: _ClassVar[SignalingPacketType]
    OFFER: _ClassVar[SignalingPacketType]
    ANSWER: _ClassVar[SignalingPacketType]
    ICE_CANDIDATE: _ClassVar[SignalingPacketType]
GATHER: SignalingPacketType
ACTIVE_OFFERS: SignalingPacketType
OFFER: SignalingPacketType
ANSWER: SignalingPacketType
ICE_CANDIDATE: SignalingPacketType

class PacketIdentity(_message.Message):
    __slots__ = ("origin", "token", "additionalIdentifiers")
    class PacketOriginationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVED: _ClassVar[PacketIdentity.PacketOriginationType]
        SERVICES: _ClassVar[PacketIdentity.PacketOriginationType]
        MACHINE_DIRECT: _ClassVar[PacketIdentity.PacketOriginationType]
        MACHINE_PROXY: _ClassVar[PacketIdentity.PacketOriginationType]
        PROCESS: _ClassVar[PacketIdentity.PacketOriginationType]
        DASHBOARD: _ClassVar[PacketIdentity.PacketOriginationType]
        API: _ClassVar[PacketIdentity.PacketOriginationType]
        UNKNOWN: _ClassVar[PacketIdentity.PacketOriginationType]
    RESERVED: PacketIdentity.PacketOriginationType
    SERVICES: PacketIdentity.PacketOriginationType
    MACHINE_DIRECT: PacketIdentity.PacketOriginationType
    MACHINE_PROXY: PacketIdentity.PacketOriginationType
    PROCESS: PacketIdentity.PacketOriginationType
    DASHBOARD: PacketIdentity.PacketOriginationType
    API: PacketIdentity.PacketOriginationType
    UNKNOWN: PacketIdentity.PacketOriginationType
    class AdditionalIdentifiersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALIDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    origin: PacketIdentity.PacketOriginationType
    token: str
    additionalIdentifiers: _containers.ScalarMap[str, str]
    def __init__(self, origin: _Optional[_Union[PacketIdentity.PacketOriginationType, str]] = ..., token: _Optional[str] = ..., additionalIdentifiers: _Optional[_Mapping[str, str]] = ...) -> None: ...

class WebsocketPacket(_message.Message):
    __slots__ = ("action", "identity", "payload", "message", "connectionId", "requestId")
    class PacketType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVED: _ClassVar[WebsocketPacket.PacketType]
        ACKNOWLEDGED: _ClassVar[WebsocketPacket.PacketType]
        START: _ClassVar[WebsocketPacket.PacketType]
        INFO: _ClassVar[WebsocketPacket.PacketType]
        END: _ClassVar[WebsocketPacket.PacketType]
        CREATE_ACCESS: _ClassVar[WebsocketPacket.PacketType]
        CREATE_SOURCE: _ClassVar[WebsocketPacket.PacketType]
        CREATE_SUBSCRIBER: _ClassVar[WebsocketPacket.PacketType]
        SOURCE_LOG: _ClassVar[WebsocketPacket.PacketType]
        SOURCE_REPORT: _ClassVar[WebsocketPacket.PacketType]
        SOURCE_CONTROLS: _ClassVar[WebsocketPacket.PacketType]
        SOURCE_UPDATE: _ClassVar[WebsocketPacket.PacketType]
        SOURCE_INFO: _ClassVar[WebsocketPacket.PacketType]
        PROCESS_IDENTIFY: _ClassVar[WebsocketPacket.PacketType]
        PROCESS_LOG: _ClassVar[WebsocketPacket.PacketType]
        PROCESS_REPORT: _ClassVar[WebsocketPacket.PacketType]
        PROCESS_CONTROLS: _ClassVar[WebsocketPacket.PacketType]
        SUBSCRIBER_UPDATE: _ClassVar[WebsocketPacket.PacketType]
        SUBSCRIBER_DELETE: _ClassVar[WebsocketPacket.PacketType]
        SUBSCRIPTION_DATA: _ClassVar[WebsocketPacket.PacketType]
        SUBSCRIPTION_PARTIAL: _ClassVar[WebsocketPacket.PacketType]
        ACCESS_UPDATE: _ClassVar[WebsocketPacket.PacketType]
        ACCESS_INFO: _ClassVar[WebsocketPacket.PacketType]
    RESERVED: WebsocketPacket.PacketType
    ACKNOWLEDGED: WebsocketPacket.PacketType
    START: WebsocketPacket.PacketType
    INFO: WebsocketPacket.PacketType
    END: WebsocketPacket.PacketType
    CREATE_ACCESS: WebsocketPacket.PacketType
    CREATE_SOURCE: WebsocketPacket.PacketType
    CREATE_SUBSCRIBER: WebsocketPacket.PacketType
    SOURCE_LOG: WebsocketPacket.PacketType
    SOURCE_REPORT: WebsocketPacket.PacketType
    SOURCE_CONTROLS: WebsocketPacket.PacketType
    SOURCE_UPDATE: WebsocketPacket.PacketType
    SOURCE_INFO: WebsocketPacket.PacketType
    PROCESS_IDENTIFY: WebsocketPacket.PacketType
    PROCESS_LOG: WebsocketPacket.PacketType
    PROCESS_REPORT: WebsocketPacket.PacketType
    PROCESS_CONTROLS: WebsocketPacket.PacketType
    SUBSCRIBER_UPDATE: WebsocketPacket.PacketType
    SUBSCRIBER_DELETE: WebsocketPacket.PacketType
    SUBSCRIPTION_DATA: WebsocketPacket.PacketType
    SUBSCRIPTION_PARTIAL: WebsocketPacket.PacketType
    ACCESS_UPDATE: WebsocketPacket.PacketType
    ACCESS_INFO: WebsocketPacket.PacketType
    ACTION_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONID_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    action: WebsocketPacket.PacketType
    identity: PacketIdentity
    payload: _any_pb2.Any
    message: str
    connectionId: str
    requestId: str
    def __init__(self, action: _Optional[_Union[WebsocketPacket.PacketType, str]] = ..., identity: _Optional[_Union[PacketIdentity, _Mapping]] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., message: _Optional[str] = ..., connectionId: _Optional[str] = ..., requestId: _Optional[str] = ...) -> None: ...

class SignalingPacket(_message.Message):
    __slots__ = ("action", "channel", "data", "target")
    class OfferData(_message.Message):
        __slots__ = ("type", "sdp")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SDP_FIELD_NUMBER: _ClassVar[int]
        type: str
        sdp: str
        def __init__(self, type: _Optional[str] = ..., sdp: _Optional[str] = ...) -> None: ...
    class AnswerData(_message.Message):
        __slots__ = ("type", "sdp")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SDP_FIELD_NUMBER: _ClassVar[int]
        type: str
        sdp: str
        def __init__(self, type: _Optional[str] = ..., sdp: _Optional[str] = ...) -> None: ...
    class IceCandidateData(_message.Message):
        __slots__ = ("candidate", "sdpMLineIndex", "sdpMid")
        CANDIDATE_FIELD_NUMBER: _ClassVar[int]
        SDPMLINEINDEX_FIELD_NUMBER: _ClassVar[int]
        SDPMID_FIELD_NUMBER: _ClassVar[int]
        candidate: str
        sdpMLineIndex: int
        sdpMid: str
        def __init__(self, candidate: _Optional[str] = ..., sdpMLineIndex: _Optional[int] = ..., sdpMid: _Optional[str] = ...) -> None: ...
    class GatherData(_message.Message):
        __slots__ = ("activeOffers",)
        ACTIVEOFFERS_FIELD_NUMBER: _ClassVar[int]
        activeOffers: _containers.RepeatedCompositeFieldContainer[SignalingPacket.OfferData]
        def __init__(self, activeOffers: _Optional[_Iterable[_Union[SignalingPacket.OfferData, _Mapping]]] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    action: SignalingPacketType
    channel: str
    data: _any_pb2.Any
    target: str
    def __init__(self, action: _Optional[_Union[SignalingPacketType, str]] = ..., channel: _Optional[str] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., target: _Optional[str] = ..., **kwargs) -> None: ...
