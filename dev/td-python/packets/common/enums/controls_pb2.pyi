from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ControlType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTROL_STRING: _ClassVar[ControlType]
    CONTROL_INT: _ClassVar[ControlType]
    CONTROL_FLOAT: _ClassVar[ControlType]
    CONTROL_TOGGLE: _ClassVar[ControlType]
    CONTROL_PULSE: _ClassVar[ControlType]
    CONTROL_MENU: _ClassVar[ControlType]
    CONTROL_COLOR: _ClassVar[ControlType]
    CONTROL_HEADER: _ClassVar[ControlType]
CONTROL_STRING: ControlType
CONTROL_INT: ControlType
CONTROL_FLOAT: ControlType
CONTROL_TOGGLE: ControlType
CONTROL_PULSE: ControlType
CONTROL_MENU: ControlType
CONTROL_COLOR: ControlType
CONTROL_HEADER: ControlType
