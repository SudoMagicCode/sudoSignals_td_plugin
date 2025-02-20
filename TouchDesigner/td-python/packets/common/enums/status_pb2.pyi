from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNKNOWN: _ClassVar[Status]
    OFFLINE: _ClassVar[Status]
    INITIALIZING: _ClassVar[Status]
    WARNING: _ClassVar[Status]
    RUNNING: _ClassVar[Status]
    ONLINE: _ClassVar[Status]

class ContactState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED_CONTACT_STATE: _ClassVar[ContactState]
    UNVERIFIED_CONTACT_STATE: _ClassVar[ContactState]
    VERIFIED_CONTACT_STATE: _ClassVar[ContactState]
    BOUNCED_CONTACT_STATE: _ClassVar[ContactState]
STATUS_UNKNOWN: Status
OFFLINE: Status
INITIALIZING: Status
WARNING: Status
RUNNING: Status
ONLINE: Status
UNDEFINED_CONTACT_STATE: ContactState
UNVERIFIED_CONTACT_STATE: ContactState
VERIFIED_CONTACT_STATE: ContactState
BOUNCED_CONTACT_STATE: ContactState
