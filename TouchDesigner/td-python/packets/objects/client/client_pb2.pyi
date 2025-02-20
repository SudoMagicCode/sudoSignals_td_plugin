from common.enums import status_pb2 as _status_pb2
from common import generic_pb2 as _generic_pb2
from objects.access_code import access_code_pb2 as _access_code_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Client(_message.Message):
    __slots__ = ("access_code", "token", "state")
    ACCESS_CODE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    access_code: _access_code_pb2.AccessCode
    token: _generic_pb2.Token
    state: _status_pb2.Status
    def __init__(self, access_code: _Optional[_Union[_access_code_pb2.AccessCode, _Mapping]] = ..., token: _Optional[_Union[_generic_pb2.Token, _Mapping]] = ..., state: _Optional[_Union[_status_pb2.Status, str]] = ...) -> None: ...
