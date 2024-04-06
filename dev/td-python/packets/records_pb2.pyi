import dynamo_pb2 as _dynamo_pb2
import fieldTypes_pb2 as _fieldTypes_pb2
import signalsOptions_pb2 as _signalsOptions_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
PAID: PaymentStatus
UNPAID: PaymentStatus
PENDING: PaymentStatus
FREE: Tier
BASIC: Tier
STANDARD: Tier
ENTERPRISE: Tier

class Account(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "email", "name", "adminViewer")
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADMINVIEWER_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    email: str
    name: str
    adminViewer: bool
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., email: _Optional[str] = ..., name: _Optional[str] = ..., adminViewer: bool = ...) -> None: ...

class Team(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "name", "ownerUuid", "isDefault", "members", "installations", "machines", "invitations")
    class MembersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Member
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Member, _Mapping]] = ...) -> None: ...
    class InstallationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InstallationLink
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[InstallationLink, _Mapping]] = ...) -> None: ...
    class MachinesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MachineLink
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MachineLink, _Mapping]] = ...) -> None: ...
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNERUUID_FIELD_NUMBER: _ClassVar[int]
    ISDEFAULT_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    INSTALLATIONS_FIELD_NUMBER: _ClassVar[int]
    MACHINES_FIELD_NUMBER: _ClassVar[int]
    INVITATIONS_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    name: str
    ownerUuid: str
    isDefault: bool
    members: _containers.MessageMap[str, Member]
    installations: _containers.MessageMap[str, InstallationLink]
    machines: _containers.MessageMap[str, MachineLink]
    invitations: _containers.RepeatedCompositeFieldContainer[Invitation]
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., ownerUuid: _Optional[str] = ..., isDefault: bool = ..., members: _Optional[_Mapping[str, Member]] = ..., installations: _Optional[_Mapping[str, InstallationLink]] = ..., machines: _Optional[_Mapping[str, MachineLink]] = ..., invitations: _Optional[_Iterable[_Union[Invitation, _Mapping]]] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "role")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVED: _ClassVar[Member.Role]
        OWNER: _ClassVar[Member.Role]
        ADMIN: _ClassVar[Member.Role]
        EDITOR: _ClassVar[Member.Role]
        VIEWER: _ClassVar[Member.Role]
    RESERVED: Member.Role
    OWNER: Member.Role
    ADMIN: Member.Role
    EDITOR: Member.Role
    VIEWER: Member.Role
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    role: Member.Role
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., role: _Optional[_Union[Member.Role, str]] = ...) -> None: ...

class Invitation(_message.Message):
    __slots__ = ("dynamoLookup", "email", "role")
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVED: _ClassVar[Invitation.Role]
        OWNER: _ClassVar[Invitation.Role]
        ADMIN: _ClassVar[Invitation.Role]
        EDITOR: _ClassVar[Invitation.Role]
        VIEWER: _ClassVar[Invitation.Role]
    RESERVED: Invitation.Role
    OWNER: Invitation.Role
    ADMIN: Invitation.Role
    EDITOR: Invitation.Role
    VIEWER: Invitation.Role
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    email: str
    role: Invitation.Role
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., email: _Optional[str] = ..., role: _Optional[_Union[Invitation.Role, str]] = ...) -> None: ...

class Installation(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "name", "status", "teamUuid", "teamName", "machines", "logs", "reports", "savedStates", "events", "controls", "alert_rules", "report_rules", "log_rules")
    class MachinesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MachineLink
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MachineLink, _Mapping]] = ...) -> None: ...
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TEAMUUID_FIELD_NUMBER: _ClassVar[int]
    TEAMNAME_FIELD_NUMBER: _ClassVar[int]
    MACHINES_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    SAVEDSTATES_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    ALERT_RULES_FIELD_NUMBER: _ClassVar[int]
    REPORT_RULES_FIELD_NUMBER: _ClassVar[int]
    LOG_RULES_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    name: str
    status: _fieldTypes_pb2.StatusTypes
    teamUuid: str
    teamName: str
    machines: _containers.MessageMap[str, MachineLink]
    logs: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Log]
    reports: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Report]
    savedStates: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.SavedState]
    events: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Event]
    controls: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Control]
    alert_rules: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Alert_Rule]
    report_rules: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Report_Rule]
    log_rules: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Log_Rule]
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_fieldTypes_pb2.StatusTypes, str]] = ..., teamUuid: _Optional[str] = ..., teamName: _Optional[str] = ..., machines: _Optional[_Mapping[str, MachineLink]] = ..., logs: _Optional[_Iterable[_Union[_fieldTypes_pb2.Log, _Mapping]]] = ..., reports: _Optional[_Iterable[_Union[_fieldTypes_pb2.Report, _Mapping]]] = ..., savedStates: _Optional[_Iterable[_Union[_fieldTypes_pb2.SavedState, _Mapping]]] = ..., events: _Optional[_Iterable[_Union[_fieldTypes_pb2.Event, _Mapping]]] = ..., controls: _Optional[_Iterable[_Union[_fieldTypes_pb2.Control, _Mapping]]] = ..., alert_rules: _Optional[_Iterable[_Union[_fieldTypes_pb2.Alert_Rule, _Mapping]]] = ..., report_rules: _Optional[_Iterable[_Union[_fieldTypes_pb2.Report_Rule, _Mapping]]] = ..., log_rules: _Optional[_Iterable[_Union[_fieldTypes_pb2.Log_Rule, _Mapping]]] = ...) -> None: ...

class InstallationLink(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "name", "status")
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    name: str
    status: _fieldTypes_pb2.StatusTypes
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_fieldTypes_pb2.StatusTypes, str]] = ...) -> None: ...

class Machine(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "name", "status", "installationUuid", "installationName", "teamUuid", "teamName", "connection", "lastUpdated", "latestLog", "latestReport", "systemInfo", "activeProfile", "processes", "profiles", "alert_rules", "logs", "reports")
    class ProcessesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _fieldTypes_pb2.Process
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_fieldTypes_pb2.Process, _Mapping]] = ...) -> None: ...
    class ProfilesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _fieldTypes_pb2.Profile
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_fieldTypes_pb2.Profile, _Mapping]] = ...) -> None: ...
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INSTALLATIONUUID_FIELD_NUMBER: _ClassVar[int]
    INSTALLATIONNAME_FIELD_NUMBER: _ClassVar[int]
    TEAMUUID_FIELD_NUMBER: _ClassVar[int]
    TEAMNAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    LASTUPDATED_FIELD_NUMBER: _ClassVar[int]
    LATESTLOG_FIELD_NUMBER: _ClassVar[int]
    LATESTREPORT_FIELD_NUMBER: _ClassVar[int]
    SYSTEMINFO_FIELD_NUMBER: _ClassVar[int]
    ACTIVEPROFILE_FIELD_NUMBER: _ClassVar[int]
    PROCESSES_FIELD_NUMBER: _ClassVar[int]
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    ALERT_RULES_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    name: str
    status: _fieldTypes_pb2.StatusTypes
    installationUuid: str
    installationName: str
    teamUuid: str
    teamName: str
    connection: _fieldTypes_pb2.SourceConnection
    lastUpdated: int
    latestLog: _fieldTypes_pb2.Log
    latestReport: _fieldTypes_pb2.Report
    systemInfo: _struct_pb2.Struct
    activeProfile: _fieldTypes_pb2.Profile
    processes: _containers.MessageMap[str, _fieldTypes_pb2.Process]
    profiles: _containers.MessageMap[str, _fieldTypes_pb2.Profile]
    alert_rules: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Alert_Rule]
    logs: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Log]
    reports: _containers.RepeatedCompositeFieldContainer[_fieldTypes_pb2.Report]
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_fieldTypes_pb2.StatusTypes, str]] = ..., installationUuid: _Optional[str] = ..., installationName: _Optional[str] = ..., teamUuid: _Optional[str] = ..., teamName: _Optional[str] = ..., connection: _Optional[_Union[_fieldTypes_pb2.SourceConnection, _Mapping]] = ..., lastUpdated: _Optional[int] = ..., latestLog: _Optional[_Union[_fieldTypes_pb2.Log, _Mapping]] = ..., latestReport: _Optional[_Union[_fieldTypes_pb2.Report, _Mapping]] = ..., systemInfo: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., activeProfile: _Optional[_Union[_fieldTypes_pb2.Profile, _Mapping]] = ..., processes: _Optional[_Mapping[str, _fieldTypes_pb2.Process]] = ..., profiles: _Optional[_Mapping[str, _fieldTypes_pb2.Profile]] = ..., alert_rules: _Optional[_Iterable[_Union[_fieldTypes_pb2.Alert_Rule, _Mapping]]] = ..., logs: _Optional[_Iterable[_Union[_fieldTypes_pb2.Log, _Mapping]]] = ..., reports: _Optional[_Iterable[_Union[_fieldTypes_pb2.Report, _Mapping]]] = ...) -> None: ...

class MachineLink(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "name", "status")
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    name: str
    status: _fieldTypes_pb2.StatusTypes
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[_fieldTypes_pb2.StatusTypes, str]] = ...) -> None: ...

class Client(_message.Message):
    __slots__ = ("dynamoLookup", "connected", "hasToken", "accessCode", "token")
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    HASTOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESSCODE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    connected: bool
    hasToken: bool
    accessCode: str
    token: str
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., connected: bool = ..., hasToken: bool = ..., accessCode: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class Subscription(_message.Message):
    __slots__ = ("dynamoLookup", "uuid", "handle", "token", "listening")
    DYNAMOLOOKUP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    LISTENING_FIELD_NUMBER: _ClassVar[int]
    dynamoLookup: _dynamo_pb2.DynamoRecord
    uuid: str
    handle: str
    token: str
    listening: str
    def __init__(self, dynamoLookup: _Optional[_Union[_dynamo_pb2.DynamoRecord, _Mapping]] = ..., uuid: _Optional[str] = ..., handle: _Optional[str] = ..., token: _Optional[str] = ..., listening: _Optional[str] = ...) -> None: ...
