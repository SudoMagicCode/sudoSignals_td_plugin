from common import dynamo_pb2 as _dynamo_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from common import signalsOptions_pb2 as _signalsOptions_pb2
from common import signalsEnums_pb2 as _signalsEnums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Document(_message.Message):
    __slots__ = ("dynamoLookup", "encoding", "data")
    class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BYTES: _ClassVar[Document.Encoding]
        JSON: _ClassVar[Document.Encoding]
    BYTES: Document.Encoding
    JSON: Document.Encoding
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    encoding: Document.Encoding
    data: str
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., encoding: _Optional[_Union[Document.Encoding, str]] = ..., data: _Optional[str] = ...) -> None: ...

class DataFrame(_message.Message):
    __slots__ = ("name", "fields")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    fields: _containers.RepeatedCompositeFieldContainer[DataField]
    def __init__(self, name: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[DataField, _Mapping]]] = ...) -> None: ...

class DataField(_message.Message):
    __slots__ = ("name", "type", "values")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: _signalsEnums_pb2.DataFieldTypes
    values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_signalsEnums_pb2.DataFieldTypes, str]] = ..., values: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ...) -> None: ...

class Log(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "level", "message")
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    level: _signalsEnums_pb2.LogLevel
    message: str
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., level: _Optional[_Union[_signalsEnums_pb2.LogLevel, str]] = ..., message: _Optional[str] = ...) -> None: ...

class Report(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "data")
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    data: DataFrame
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., data: _Optional[_Union[DataFrame, _Mapping]] = ...) -> None: ...

class SavedState(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class ControlPage(_message.Message):
    __slots__ = ("uuid", "name", "controls")
    class ControlsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Control
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Control, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    controls: _containers.MessageMap[int, Control]
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., controls: _Optional[_Mapping[int, Control]] = ...) -> None: ...

class Control(_message.Message):
    __slots__ = ("uuid", "controlType", "label", "entityReference", "values", "menuOptions")
    class EntityReferenceEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MenuOptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    CONTROLTYPE_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ENTITYREFERENCE_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    MENUOPTIONS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    controlType: _signalsEnums_pb2.ControlType
    label: str
    entityReference: _containers.ScalarMap[str, str]
    values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    menuOptions: _containers.ScalarMap[str, str]
    def __init__(self, uuid: _Optional[str] = ..., controlType: _Optional[_Union[_signalsEnums_pb2.ControlType, str]] = ..., label: _Optional[str] = ..., entityReference: _Optional[_Mapping[str, str]] = ..., values: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ..., menuOptions: _Optional[_Mapping[str, str]] = ...) -> None: ...

class Alert_Rule(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class Report_Rule(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class Log_Rule(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class Profile(_message.Message):
    __slots__ = ("uuid", "name", "token", "processConfigs")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROCESSCONFIGS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    token: str
    processConfigs: _containers.RepeatedCompositeFieldContainer[ProcessConfig]
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., token: _Optional[str] = ..., processConfigs: _Optional[_Iterable[_Union[ProcessConfig, _Mapping]]] = ...) -> None: ...

class Process(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "name", "status", "software", "softwareVersion", "pluginVersion", "config", "latestLog", "latestReport", "controlPages", "logs", "reports")
    class ControlPagesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ControlPage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ControlPage, _Mapping]] = ...) -> None: ...
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_FIELD_NUMBER: _ClassVar[int]
    SOFTWAREVERSION_FIELD_NUMBER: _ClassVar[int]
    PLUGINVERSION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LATESTLOG_FIELD_NUMBER: _ClassVar[int]
    LATESTREPORT_FIELD_NUMBER: _ClassVar[int]
    CONTROLPAGES_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    name: str
    status: _signalsEnums_pb2.Status
    software: str
    softwareVersion: str
    pluginVersion: str
    config: ProcessConfig
    latestLog: Log
    latestReport: Report
    controlPages: _containers.MessageMap[str, ControlPage]
    logs: _containers.RepeatedCompositeFieldContainer[Log]
    reports: _containers.RepeatedCompositeFieldContainer[Report]
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_signalsEnums_pb2.Status, str]] = ..., software: _Optional[str] = ..., softwareVersion: _Optional[str] = ..., pluginVersion: _Optional[str] = ..., config: _Optional[_Union[ProcessConfig, _Mapping]] = ..., latestLog: _Optional[_Union[Log, _Mapping]] = ..., latestReport: _Optional[_Union[Report, _Mapping]] = ..., controlPages: _Optional[_Mapping[str, ControlPage]] = ..., logs: _Optional[_Iterable[_Union[Log, _Mapping]]] = ..., reports: _Optional[_Iterable[_Union[Report, _Mapping]]] = ...) -> None: ...

class ProcessConfig(_message.Message):
    __slots__ = ("uuid", "name", "startCmd", "processPath", "autoStart", "autoRestart", "restartLimit", "envVars")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STARTCMD_FIELD_NUMBER: _ClassVar[int]
    PROCESSPATH_FIELD_NUMBER: _ClassVar[int]
    AUTOSTART_FIELD_NUMBER: _ClassVar[int]
    AUTORESTART_FIELD_NUMBER: _ClassVar[int]
    RESTARTLIMIT_FIELD_NUMBER: _ClassVar[int]
    ENVVARS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    startCmd: str
    processPath: str
    autoStart: bool
    autoRestart: bool
    restartLimit: int
    envVars: _containers.RepeatedCompositeFieldContainer[EnvVars]
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., startCmd: _Optional[str] = ..., processPath: _Optional[str] = ..., autoStart: bool = ..., autoRestart: bool = ..., restartLimit: _Optional[int] = ..., envVars: _Optional[_Iterable[_Union[EnvVars, _Mapping]]] = ...) -> None: ...

class EnvVars(_message.Message):
    __slots__ = ("label", "value")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    label: str
    value: str
    def __init__(self, label: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class AccountView(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SourceConnection(_message.Message):
    __slots__ = ("dynamoLookup", "status", "token", "handle")
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    status: _signalsEnums_pb2.Status
    token: str
    handle: str
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., status: _Optional[_Union[_signalsEnums_pb2.Status, str]] = ..., token: _Optional[str] = ..., handle: _Optional[str] = ...) -> None: ...
