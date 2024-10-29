from google.protobuf import timestamp_pb2 as _timestamp_pb2
from objects.installation import installation_fields_pb2 as _installation_fields_pb2
from common import generic_pb2 as _generic_pb2
from objects.alerts import alerts_pb2 as _alerts_pb2
from objects.machine import machine_pb2 as _machine_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Installation(_message.Message):
    __slots__ = ("uuid", "name", "status", "image", "alert_rules", "machines", "date_created", "provenance")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ALERT_RULES_FIELD_NUMBER: _ClassVar[int]
    MACHINES_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    name: _generic_pb2.Name
    status: _installation_fields_pb2.InstallationStatus
    image: _generic_pb2.Image
    alert_rules: _alerts_pb2.AlertRuleCollection
    machines: _machine_pb2.MachineCollection
    date_created: _timestamp_pb2.Timestamp
    provenance: _generic_pb2.Provenance
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ..., status: _Optional[_Union[_installation_fields_pb2.InstallationStatus, _Mapping]] = ..., image: _Optional[_Union[_generic_pb2.Image, _Mapping]] = ..., alert_rules: _Optional[_Union[_alerts_pb2.AlertRuleCollection, _Mapping]] = ..., machines: _Optional[_Union[_machine_pb2.MachineCollection, _Mapping]] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., provenance: _Optional[_Union[_generic_pb2.Provenance, _Mapping]] = ...) -> None: ...

class InstallationCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Installation
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Installation, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, Installation]
    def __init__(self, options: _Optional[_Mapping[str, Installation]] = ...) -> None: ...
