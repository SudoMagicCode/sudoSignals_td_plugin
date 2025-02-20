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
    EDITOR: _ClassVar[Role]
    ADMIN: _ClassVar[Role]
    OWNER: _ClassVar[Role]
    SUDO: _ClassVar[Role]

class DataFieldTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_FIELD_UNKNOWN: _ClassVar[DataFieldTypes]
    TIME: _ClassVar[DataFieldTypes]
    NUMBER: _ClassVar[DataFieldTypes]
    STRING: _ClassVar[DataFieldTypes]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNKNOWN: _ClassVar[Status]
    OFFLINE: _ClassVar[Status]
    INITIALIZING: _ClassVar[Status]
    WARNING: _ClassVar[Status]
    ONLINE: _ClassVar[Status]

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG: _ClassVar[LogLevel]
    INFO: _ClassVar[LogLevel]
    WARN: _ClassVar[LogLevel]
    CRIT: _ClassVar[LogLevel]
    ALERT: _ClassVar[LogLevel]

class LogOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_ORIGIN_UNKNOWN: _ClassVar[LogOrigin]
    SERVICES: _ClassVar[LogOrigin]
    MACHINE: _ClassVar[LogOrigin]
    PROCESS: _ClassVar[LogOrigin]

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

class SubscriptionTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    TEAM_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    INSTALLATION_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    MACHINE_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    MACHINE_REPORT_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    MACHINE_LOG_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    PROCESS_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    PROCESS_REPORT_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    PROCESS_CONTROL_SUBSCRIPTION: _ClassVar[SubscriptionTypes]
    ACCOUNT_SUBSCRIPTION: _ClassVar[SubscriptionTypes]

class MachineActions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED_MACHINE_ACTION: _ClassVar[MachineActions]
    START_ALL_PROCESSES: _ClassVar[MachineActions]
    STOP_ALL_PROCESSES: _ClassVar[MachineActions]
    RESTART_MACHINE: _ClassVar[MachineActions]
    CHANGE_PROFILE: _ClassVar[MachineActions]
    START_PROCESS: _ClassVar[MachineActions]
    STOP_PROCESS: _ClassVar[MachineActions]
    RESTART_PROCESS: _ClassVar[MachineActions]

class ClientState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED_CLIENT_STATE: _ClassVar[ClientState]
    NOT_CONNECTED: _ClassVar[ClientState]
    CONNECTED: _ClassVar[ClientState]

class ContactState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED_CONTACT_STATE: _ClassVar[ContactState]
    UNVERIFIED_CONTACT_STATE: _ClassVar[ContactState]
    VERIFIED_CONTACT_STATE: _ClassVar[ContactState]
    BOUNCED_CONTACT_STATE: _ClassVar[ContactState]
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
EDITOR: Role
ADMIN: Role
OWNER: Role
SUDO: Role
DATA_FIELD_UNKNOWN: DataFieldTypes
TIME: DataFieldTypes
NUMBER: DataFieldTypes
STRING: DataFieldTypes
STATUS_UNKNOWN: Status
OFFLINE: Status
INITIALIZING: Status
WARNING: Status
ONLINE: Status
LOG: LogLevel
INFO: LogLevel
WARN: LogLevel
CRIT: LogLevel
ALERT: LogLevel
LOG_ORIGIN_UNKNOWN: LogOrigin
SERVICES: LogOrigin
MACHINE: LogOrigin
PROCESS: LogOrigin
CONTROL_STRING: ControlType
CONTROL_INT: ControlType
CONTROL_FLOAT: ControlType
CONTROL_TOGGLE: ControlType
CONTROL_PULSE: ControlType
CONTROL_MENU: ControlType
CONTROL_COLOR: ControlType
CONTROL_HEADER: ControlType
UNDEFINED_SUBSCRIPTION: SubscriptionTypes
TEAM_SUBSCRIPTION: SubscriptionTypes
INSTALLATION_SUBSCRIPTION: SubscriptionTypes
MACHINE_SUBSCRIPTION: SubscriptionTypes
MACHINE_REPORT_SUBSCRIPTION: SubscriptionTypes
MACHINE_LOG_SUBSCRIPTION: SubscriptionTypes
PROCESS_SUBSCRIPTION: SubscriptionTypes
PROCESS_REPORT_SUBSCRIPTION: SubscriptionTypes
PROCESS_CONTROL_SUBSCRIPTION: SubscriptionTypes
ACCOUNT_SUBSCRIPTION: SubscriptionTypes
UNDEFINED_MACHINE_ACTION: MachineActions
START_ALL_PROCESSES: MachineActions
STOP_ALL_PROCESSES: MachineActions
RESTART_MACHINE: MachineActions
CHANGE_PROFILE: MachineActions
START_PROCESS: MachineActions
STOP_PROCESS: MachineActions
RESTART_PROCESS: MachineActions
UNDEFINED_CLIENT_STATE: ClientState
NOT_CONNECTED: ClientState
CONNECTED: ClientState
UNDEFINED_CONTACT_STATE: ContactState
UNVERIFIED_CONTACT_STATE: ContactState
VERIFIED_CONTACT_STATE: ContactState
BOUNCED_CONTACT_STATE: ContactState
