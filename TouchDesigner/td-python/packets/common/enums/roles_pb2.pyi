from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIEWER: _ClassVar[Role]
    EDITOR: _ClassVar[Role]
    ADMIN: _ClassVar[Role]
    OWNER: _ClassVar[Role]
    SUDO: _ClassVar[Role]
VIEWER: Role
EDITOR: Role
ADMIN: Role
OWNER: Role
SUDO: Role
