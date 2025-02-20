from common import generic_pb2 as _generic_pb2
from objects.report import report_fields_pb2 as _report_fields_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Report(_message.Message):
    __slots__ = ("uuid", "data")
    UUID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    data: _report_fields_pb2.DataFrame
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., data: _Optional[_Union[_report_fields_pb2.DataFrame, _Mapping]] = ...) -> None: ...

class ReportCollection(_message.Message):
    __slots__ = ("options",)
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.RepeatedCompositeFieldContainer[Report]
    def __init__(self, options: _Optional[_Iterable[_Union[Report, _Mapping]]] = ...) -> None: ...
