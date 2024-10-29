from common import generic_pb2 as _generic_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionPayload(_message.Message):
    __slots__ = ("account_uuid", "connection_token")
    ACCOUNT_UUID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_uuid: _generic_pb2.Uuid
    connection_token: _generic_pb2.Token
    def __init__(self, account_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., connection_token: _Optional[_Union[_generic_pb2.Token, _Mapping]] = ...) -> None: ...

class OAuthPayload(_message.Message):
    __slots__ = ("code", "refresh_token", "redirect_uri")
    CODE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    code: str
    refresh_token: str
    redirect_uri: str
    def __init__(self, code: _Optional[str] = ..., refresh_token: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...
