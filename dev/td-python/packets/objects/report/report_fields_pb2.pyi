from google.protobuf import struct_pb2 as _struct_pb2
from common.enums import data_field_pb2 as _data_field_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    type: _data_field_pb2.DataFieldTypes
    values: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[_data_field_pb2.DataFieldTypes, str]] = ..., values: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]] = ...) -> None: ...
