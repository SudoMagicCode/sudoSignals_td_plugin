from objects.controls import controls_pb2 as _controls_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessPayload(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class ProcessLogPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProcessReportPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProcessControlPayload(_message.Message):
    __slots__ = ("data",)
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _controls_pb2.ControlPage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_controls_pb2.ControlPage, _Mapping]] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.MessageMap[str, _controls_pb2.ControlPage]
    def __init__(self, data: _Optional[_Mapping[str, _controls_pb2.ControlPage]] = ...) -> None: ...
