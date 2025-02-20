from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

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
