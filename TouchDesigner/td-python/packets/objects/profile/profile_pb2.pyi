from common import generic_pb2 as _generic_pb2
from objects.process import process_fields_pb2 as _process_fields_pb2
from common.options import message_options_pb2 as _message_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfileName(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class Profile(_message.Message):
    __slots__ = ("uuid", "name", "token", "process_configs")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROCESS_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    name: ProfileName
    token: _generic_pb2.Token
    process_configs: ProcessConfigCollection
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., name: _Optional[_Union[ProfileName, _Mapping]] = ..., token: _Optional[_Union[_generic_pb2.Token, _Mapping]] = ..., process_configs: _Optional[_Union[ProcessConfigCollection, _Mapping]] = ...) -> None: ...

class ProfileCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Profile
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Profile, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, Profile]
    def __init__(self, options: _Optional[_Mapping[str, Profile]] = ...) -> None: ...

class ProcessConfigCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _process_fields_pb2.ProcessConfig
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_process_fields_pb2.ProcessConfig, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, _process_fields_pb2.ProcessConfig]
    def __init__(self, options: _Optional[_Mapping[str, _process_fields_pb2.ProcessConfig]] = ...) -> None: ...
