from google.protobuf import timestamp_pb2 as _timestamp_pb2
from common import generic_pb2 as _generic_pb2
from objects.report import report_pb2 as _report_pb2
from objects.log import log_pb2 as _log_pb2
from objects.controls import controls_pb2 as _controls_pb2
from objects.process import process_fields_pb2 as _process_fields_pb2
from common.options import message_options_pb2 as _message_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Process(_message.Message):
    __slots__ = ("uuid", "name", "status", "last_start", "program_info", "config", "latest_log", "latest_report", "control_pages")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_START_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_INFO_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LATEST_LOG_FIELD_NUMBER: _ClassVar[int]
    LATEST_REPORT_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PAGES_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    name: _generic_pb2.Name
    status: _process_fields_pb2.ProcessStatus
    last_start: _timestamp_pb2.Timestamp
    program_info: _process_fields_pb2.ProgramInfo
    config: _process_fields_pb2.ProcessConfig
    latest_log: _log_pb2.Log
    latest_report: _report_pb2.Report
    control_pages: _controls_pb2.ControlPageCollection
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ..., status: _Optional[_Union[_process_fields_pb2.ProcessStatus, _Mapping]] = ..., last_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., program_info: _Optional[_Union[_process_fields_pb2.ProgramInfo, _Mapping]] = ..., config: _Optional[_Union[_process_fields_pb2.ProcessConfig, _Mapping]] = ..., latest_log: _Optional[_Union[_log_pb2.Log, _Mapping]] = ..., latest_report: _Optional[_Union[_report_pb2.Report, _Mapping]] = ..., control_pages: _Optional[_Union[_controls_pb2.ControlPageCollection, _Mapping]] = ...) -> None: ...

class ProcessCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Process
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Process, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, Process]
    def __init__(self, options: _Optional[_Mapping[str, Process]] = ...) -> None: ...
