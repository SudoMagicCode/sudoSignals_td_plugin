from google.protobuf import timestamp_pb2 as _timestamp_pb2
from common import generic_pb2 as _generic_pb2
from common.enums import packets_pb2 as _packets_pb2
from common.enums import logs_pb2 as _logs_pb2
from objects.log import log_fields_pb2 as _log_fields_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Log(_message.Message):
    __slots__ = ("uuid", "time", "level", "message", "origin", "entity_reference")
    UUID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    ENTITY_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    time: _timestamp_pb2.Timestamp
    level: _logs_pb2.LogLevel
    message: _log_fields_pb2.LogMessage
    origin: _packets_pb2.PacketOriginationType
    entity_reference: _generic_pb2.EntityReference
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., level: _Optional[_Union[_logs_pb2.LogLevel, str]] = ..., message: _Optional[_Union[_log_fields_pb2.LogMessage, _Mapping]] = ..., origin: _Optional[_Union[_packets_pb2.PacketOriginationType, str]] = ..., entity_reference: _Optional[_Union[_generic_pb2.EntityReference, _Mapping]] = ...) -> None: ...

class LogCollection(_message.Message):
    __slots__ = ("options",)
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedCompositeFieldContainer[Log]
    def __init__(self, options: _Optional[_Iterable[_Union[Log, _Mapping]]] = ...) -> None: ...
