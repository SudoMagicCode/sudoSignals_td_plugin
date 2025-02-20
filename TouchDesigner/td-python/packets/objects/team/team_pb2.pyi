from google.protobuf import timestamp_pb2 as _timestamp_pb2
from objects.team import team_fields_pb2 as _team_fields_pb2
from common import generic_pb2 as _generic_pb2
from objects.machine import machine_pb2 as _machine_pb2
from objects.installation import installation_pb2 as _installation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Team(_message.Message):
    __slots__ = ("uuid", "name", "owner_uuid", "members", "invitations", "machines", "installations", "date_created", "provenance", "is_default")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_UUID_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    INVITATIONS_FIELD_NUMBER: _ClassVar[int]
    MACHINES_FIELD_NUMBER: _ClassVar[int]
    INSTALLATIONS_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    PROVENANCE_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    name: _generic_pb2.Name
    owner_uuid: _generic_pb2.Uuid
    members: _team_fields_pb2.MemberCollection
    invitations: _team_fields_pb2.InvitationCollection
    machines: _machine_pb2.MachineCollection
    installations: _installation_pb2.InstallationCollection
    date_created: _timestamp_pb2.Timestamp
    provenance: _generic_pb2.Provenance
    is_default: bool
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ..., owner_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., members: _Optional[_Union[_team_fields_pb2.MemberCollection, _Mapping]] = ..., invitations: _Optional[_Union[_team_fields_pb2.InvitationCollection, _Mapping]] = ..., machines: _Optional[_Union[_machine_pb2.MachineCollection, _Mapping]] = ..., installations: _Optional[_Union[_installation_pb2.InstallationCollection, _Mapping]] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., provenance: _Optional[_Union[_generic_pb2.Provenance, _Mapping]] = ..., is_default: bool = ...) -> None: ...

class TeamCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Team
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Team, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, Team]
    def __init__(self, options: _Optional[_Mapping[str, Team]] = ...) -> None: ...
