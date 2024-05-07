from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAID: _ClassVar[PaymentStatus]
    UNPAID: _ClassVar[PaymentStatus]
    PENDING: _ClassVar[PaymentStatus]

class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FREE: _ClassVar[Tier]
    BASIC: _ClassVar[Tier]
    STANDARD: _ClassVar[Tier]
    ENTERPRISE: _ClassVar[Tier]

class AccountTheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT: _ClassVar[AccountTheme]
    LIGHT: _ClassVar[AccountTheme]
    DARK: _ClassVar[AccountTheme]

class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIEWER: _ClassVar[Role]
    OWNER: _ClassVar[Role]
    ADMIN: _ClassVar[Role]
    EDITOR: _ClassVar[Role]

class DataFieldTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIME: _ClassVar[DataFieldTypes]
    NUMBER: _ClassVar[DataFieldTypes]
    STRING: _ClassVar[DataFieldTypes]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNKNOWN: _ClassVar[Status]
    ONLINE: _ClassVar[Status]
    OFFLINE: _ClassVar[Status]
    WARNING: _ClassVar[Status]

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG: _ClassVar[LogLevel]
    INFO: _ClassVar[LogLevel]
    WARN: _ClassVar[LogLevel]
    CRIT: _ClassVar[LogLevel]

class ControlType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTROL_STRING: _ClassVar[ControlType]
    CONTROL_INT: _ClassVar[ControlType]
    CONTROL_FLOAT: _ClassVar[ControlType]
    CONTROL_TOGGLE: _ClassVar[ControlType]
    CONTROL_PULSE: _ClassVar[ControlType]
    CONTROL_MENU: _ClassVar[ControlType]

class SubscriptionTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    TEAM_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    INSTALLATION_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    MACHINE_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
PAID: PaymentStatus
UNPAID: PaymentStatus
PENDING: PaymentStatus
FREE: Tier
BASIC: Tier
STANDARD: Tier
ENTERPRISE: Tier
DEFAULT: AccountTheme
LIGHT: AccountTheme
DARK: AccountTheme
VIEWER: Role
OWNER: Role
ADMIN: Role
EDITOR: Role
TIME: DataFieldTypes
NUMBER: DataFieldTypes
STRING: DataFieldTypes
STATUS_UNKNOWN: Status
ONLINE: Status
OFFLINE: Status
WARNING: Status
LOG: LogLevel
INFO: LogLevel
WARN: LogLevel
CRIT: LogLevel
CONTROL_STRING: ControlType
CONTROL_INT: ControlType
CONTROL_FLOAT: ControlType
CONTROL_TOGGLE: ControlType
CONTROL_PULSE: ControlType
CONTROL_MENU: ControlType
UNDEFINED_SUBSCRIPTION: SubscriptionTypes
TEAM_SUBSCRIPTION: SubscriptionTypes
INSTALLATION_SUBSCRIPTION: SubscriptionTypes
MACHINE_SUBSCRIPTION: SubscriptionTypes
