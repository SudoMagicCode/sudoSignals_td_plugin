from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DataFieldTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_FIELD_UNKNOWN: _ClassVar[DataFieldTypes]
    TIME: _ClassVar[DataFieldTypes]
    NUMBER: _ClassVar[DataFieldTypes]
    STRING: _ClassVar[DataFieldTypes]
DATA_FIELD_UNKNOWN: DataFieldTypes
TIME: DataFieldTypes
NUMBER: DataFieldTypes
STRING: DataFieldTypes
