from common.enums import status_pb2 as _status_pb2
from common import generic_pb2 as _generic_pb2
from objects.controls import controls_pb2 as _controls_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MachineStatus(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: _status_pb2.Status
    def __init__(self, state: _Optional[_Union[_status_pb2.Status, str]] = ...) -> None: ...

class SourceConnection(_message.Message):
    __slots__ = ("status", "token", "handle")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    token: _generic_pb2.Token
    handle: _generic_pb2.ConnectionHandle
    def __init__(self, status: _Optional[_Union[_status_pb2.Status, str]] = ..., token: _Optional[_Union[_generic_pb2.Token, _Mapping]] = ..., handle: _Optional[_Union[_generic_pb2.ConnectionHandle, _Mapping]] = ...) -> None: ...

class PromotedControlCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _controls_pb2.PromotedControl
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_controls_pb2.PromotedControl, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, _controls_pb2.PromotedControl]
    def __init__(self, options: _Optional[_Mapping[str, _controls_pb2.PromotedControl]] = ...) -> None: ...
