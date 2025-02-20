from google.protobuf import any_pb2 as _any_pb2
from common.enums import packets_pb2 as _packets_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PacketIdentity(_message.Message):
    __slots__ = ("origin", "token", "additionalIdentifiers")
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
    origin: _packets_pb2.PacketOriginationType
    token: str
    additionalIdentifiers: _containers.ScalarMap[str, str]
    def __init__(self, origin: _Optional[_Union[_packets_pb2.PacketOriginationType, str]] = ..., token: _Optional[str] = ..., additionalIdentifiers: _Optional[_Mapping[str, str]] = ...) -> None: ...

class WebsocketPacket(_message.Message):
    __slots__ = ("action", "identity", "payload", "message", "connectionId", "requestId")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONID_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    action: _packets_pb2.PacketType
    identity: PacketIdentity
    payload: _any_pb2.Any
    message: str
    connectionId: str
    requestId: str
    def __init__(self, action: _Optional[_Union[_packets_pb2.PacketType, str]] = ..., identity: _Optional[_Union[PacketIdentity, _Mapping]] = ..., payload: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., message: _Optional[str] = ..., connectionId: _Optional[str] = ..., requestId: _Optional[str] = ...) -> None: ...
