from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from common import generic_pb2 as _generic_pb2
from objects.profile import profile_pb2 as _profile_pb2
from objects.process import process_pb2 as _process_pb2
from objects.alerts import alerts_pb2 as _alerts_pb2
from objects.log import log_pb2 as _log_pb2
from objects.report import report_pb2 as _report_pb2
from objects.client import client_pb2 as _client_pb2
from objects.machine import machine_fields_pb2 as _machine_fields_pb2
from common.options import message_options_pb2 as _message_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Machine(_message.Message):
    __slots__ = ("uuid", "name", "status", "last_updated", "last_boot", "date_created", "connection", "latest_log", "latest_report", "system_info", "active_profile", "profiles", "processes", "alert_rules", "client_info", "promoted_controls", "provenance")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    LAST_BOOT_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    LATEST_LOG_FIELD_NUMBER: _ClassVar[int]
    LATEST_REPORT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    ALERT_RULES_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    PROMOTED_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    name: _generic_pb2.Name
    status: _machine_fields_pb2.MachineStatus
    last_updated: _timestamp_pb2.Timestamp
    last_boot: _timestamp_pb2.Timestamp
    date_created: _timestamp_pb2.Timestamp
    connection: _machine_fields_pb2.SourceConnection
    latest_log: _log_pb2.Log
    latest_report: _report_pb2.Report
    system_info: _struct_pb2.Struct
    active_profile: _profile_pb2.Profile
    profiles: _profile_pb2.ProfileCollection
    processes: _process_pb2.ProcessCollection
    alert_rules: _alerts_pb2.AlertRuleCollection
    client_info: _client_pb2.Client
    promoted_controls: _machine_fields_pb2.PromotedControlCollection
    provenance: _generic_pb2.Provenance
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ..., status: _Optional[_Union[_machine_fields_pb2.MachineStatus, _Mapping]] = ..., last_updated: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_boot: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., connection: _Optional[_Union[_machine_fields_pb2.SourceConnection, _Mapping]] = ..., latest_log: _Optional[_Union[_log_pb2.Log, _Mapping]] = ..., latest_report: _Optional[_Union[_report_pb2.Report, _Mapping]] = ..., system_info: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., active_profile: _Optional[_Union[_profile_pb2.Profile, _Mapping]] = ..., profiles: _Optional[_Union[_profile_pb2.ProfileCollection, _Mapping]] = ..., processes: _Optional[_Union[_process_pb2.ProcessCollection, _Mapping]] = ..., alert_rules: _Optional[_Union[_alerts_pb2.AlertRuleCollection, _Mapping]] = ..., client_info: _Optional[_Union[_client_pb2.Client, _Mapping]] = ..., promoted_controls: _Optional[_Union[_machine_fields_pb2.PromotedControlCollection, _Mapping]] = ..., provenance: _Optional[_Union[_generic_pb2.Provenance, _Mapping]] = ...) -> None: ...

class MachineCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Machine
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Machine, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, Machine]
    def __init__(self, options: _Optional[_Mapping[str, Machine]] = ...) -> None: ...
