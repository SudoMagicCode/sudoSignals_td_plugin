from common import generic_pb2 as _generic_pb2
from common.enums import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessStatus(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: _status_pb2.Status
    def __init__(self, state: _Optional[_Union[_status_pb2.Status, str]] = ...) -> None: ...

class ProgramInfo(_message.Message):
    __slots__ = ("company_name", "product_name", "file_description", "product_version", "file_version", "program_path")
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_VERSION_FIELD_NUMBER: _ClassVar[int]
    FILE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_PATH_FIELD_NUMBER: _ClassVar[int]
    company_name: str
    product_name: str
    file_description: str
    product_version: str
    file_version: str
    program_path: str
    def __init__(self, company_name: _Optional[str] = ..., product_name: _Optional[str] = ..., file_description: _Optional[str] = ..., product_version: _Optional[str] = ..., file_version: _Optional[str] = ..., program_path: _Optional[str] = ...) -> None: ...

class ProcessConfig(_message.Message):
    __slots__ = ("uuid", "name", "class_lookup", "start_cmd", "process_path", "current_working_directory", "auto_start", "always_restart", "restart_limit", "index", "env_vars", "args")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLASS_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    START_CMD_FIELD_NUMBER: _ClassVar[int]
    PROCESS_PATH_FIELD_NUMBER: _ClassVar[int]
    CURRENT_WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    AUTO_START_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_RESTART_FIELD_NUMBER: _ClassVar[int]
    RESTART_LIMIT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ENV_VARS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    name: _generic_pb2.Name
    class_lookup: ClassLookup
    start_cmd: StartCMD
    process_path: ProcessPath
    current_working_directory: CurrentWorkingDirectory
    auto_start: bool
    always_restart: bool
    restart_limit: int
    index: int
    env_vars: EnvVarCollection
    args: ArgumentCollection
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ..., class_lookup: _Optional[_Union[ClassLookup, _Mapping]] = ..., start_cmd: _Optional[_Union[StartCMD, _Mapping]] = ..., process_path: _Optional[_Union[ProcessPath, _Mapping]] = ..., current_working_directory: _Optional[_Union[CurrentWorkingDirectory, _Mapping]] = ..., auto_start: bool = ..., always_restart: bool = ..., restart_limit: _Optional[int] = ..., index: _Optional[int] = ..., env_vars: _Optional[_Union[EnvVarCollection, _Mapping]] = ..., args: _Optional[_Union[ArgumentCollection, _Mapping]] = ...) -> None: ...

class ClassLookup(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class StartCMD(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class ProcessPath(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class CurrentWorkingDirectory(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class EnvVarCollection(_message.Message):
    __slots__ = ("options",)
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedCompositeFieldContainer[EnvVar]
    def __init__(self, options: _Optional[_Iterable[_Union[EnvVar, _Mapping]]] = ...) -> None: ...

class EnvVar(_message.Message):
    __slots__ = ("label", "value")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    label: str
    value: str
    def __init__(self, label: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ArgumentCollection(_message.Message):
    __slots__ = ("options",)
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedCompositeFieldContainer[Argument]
    def __init__(self, options: _Optional[_Iterable[_Union[Argument, _Mapping]]] = ...) -> None: ...

class Argument(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...
