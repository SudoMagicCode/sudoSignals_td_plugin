from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Uuid(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class Name(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class Email(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class UrlPath(_message.Message):
    __slots__ = ("base_path", "search_params", "hash_params")
    BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    HASH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    base_path: str
    search_params: str
    hash_params: str
    def __init__(self, base_path: _Optional[str] = ..., search_params: _Optional[str] = ..., hash_params: _Optional[str] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("key", "path")
    KEY_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    key: str
    path: str
    def __init__(self, key: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class Token(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ConnectionHandle(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class EntityReference(_message.Message):
    __slots__ = ("value",)
    class ValueEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.ScalarMap[str, str]
    def __init__(self, value: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Provenance(_message.Message):
    __slots__ = ("account", "team", "installation", "machine")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    account: Uuid
    team: Uuid
    installation: Uuid
    machine: Uuid
    def __init__(self, account: _Optional[_Union[Uuid, _Mapping]] = ..., team: _Optional[_Union[Uuid, _Mapping]] = ..., installation: _Optional[_Union[Uuid, _Mapping]] = ..., machine: _Optional[_Union[Uuid, _Mapping]] = ...) -> None: ...
