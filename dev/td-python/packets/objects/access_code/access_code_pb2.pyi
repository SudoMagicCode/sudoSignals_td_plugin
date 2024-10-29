from common import generic_pb2 as _generic_pb2
from objects.access_code import access_code_fields_pb2 as _access_code_fields_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessCode(_message.Message):
    __slots__ = ("uuid", "code", "handle")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    code: _access_code_fields_pb2.Code
    handle: _generic_pb2.ConnectionHandle
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., code: _Optional[_Union[_access_code_fields_pb2.Code, _Mapping]] = ..., handle: _Optional[_Union[_generic_pb2.ConnectionHandle, _Mapping]] = ...) -> None: ...
