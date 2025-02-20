from common.dynamo import fields_pb2 as _fields_pb2
from objects.account import account_pb2 as _account_pb2
from objects.installation import installation_pb2 as _installation_pb2
from objects.machine import machine_pb2 as _machine_pb2
from objects.team import team_pb2 as _team_pb2
from objects.access_code import access_code_pb2 as _access_code_pb2
from records import link_pb2 as _link_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Record(_message.Message):
    __slots__ = ("dynamo_lookup", "links", "account", "team", "machine", "installation", "access_code")
    class LinksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _link_pb2.Link
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_link_pb2.Link, _Mapping]] = ...) -> None: ...
    DYNAMO_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CODE_FIELD_NUMBER: _ClassVar[int]
    dynamo_lookup: _fields_pb2.DynamoRecord
    links: _containers.MessageMap[str, _link_pb2.Link]
    account: _account_pb2.Account
    team: _team_pb2.Team
    machine: _machine_pb2.Machine
    installation: _installation_pb2.Installation
    access_code: _access_code_pb2.AccessCode
    def __init__(self, dynamo_lookup: _Optional[_Union[_fields_pb2.DynamoRecord, _Mapping]] = ..., links: _Optional[_Mapping[str, _link_pb2.Link]] = ..., account: _Optional[_Union[_account_pb2.Account, _Mapping]] = ..., team: _Optional[_Union[_team_pb2.Team, _Mapping]] = ..., machine: _Optional[_Union[_machine_pb2.Machine, _Mapping]] = ..., installation: _Optional[_Union[_installation_pb2.Installation, _Mapping]] = ..., access_code: _Optional[_Union[_access_code_pb2.AccessCode, _Mapping]] = ...) -> None: ...
