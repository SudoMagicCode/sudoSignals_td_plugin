import fieldTypes_pb2 as _fieldTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessPayload(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class SourcePayload(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class SubscriptionPayload(_message.Message):
    __slots__ = ("partitionKey", "sortKey")
    PARTITIONKEY_FIELD_NUMBER: _ClassVar[int]
    SORTKEY_FIELD_NUMBER: _ClassVar[int]
    partitionKey: str
    sortKey: str
    def __init__(self, partitionKey: _Optional[str] = ..., sortKey: _Optional[str] = ...) -> None: ...

class ProcessPayload(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class RpcPayload(_message.Message):
    __slots__ = ("request", "response")
    class RequestEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ResponseEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    request: _containers.ScalarMap[str, str]
    response: _containers.ScalarMap[str, str]
    def __init__(self, request: _Optional[_Mapping[str, str]] = ..., response: _Optional[_Mapping[str, str]] = ...) -> None: ...

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
        value: _fieldTypes_pb2.ControlPage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_fieldTypes_pb2.ControlPage, _Mapping]] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.MessageMap[str, _fieldTypes_pb2.ControlPage]
    def __init__(self, data: _Optional[_Mapping[str, _fieldTypes_pb2.ControlPage]] = ...) -> None: ...
