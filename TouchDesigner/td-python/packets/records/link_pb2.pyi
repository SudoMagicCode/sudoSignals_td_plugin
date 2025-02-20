from common import generic_pb2 as _generic_pb2
from common.dynamo import fields_pb2 as _fields_pb2
from objects.team import member_pb2 as _member_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Link(_message.Message):
    __slots__ = ("dynamo_lookup", "installation", "machine", "member")
    DYNAMO_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    dynamo_lookup: _fields_pb2.DynamoRecord
    installation: ToInstallation
    machine: ToMachine
    member: ToMember
    def __init__(self, dynamo_lookup: _Optional[_Union[_fields_pb2.DynamoRecord, _Mapping]] = ..., installation: _Optional[_Union[ToInstallation, _Mapping]] = ..., machine: _Optional[_Union[ToMachine, _Mapping]] = ..., member: _Optional[_Union[ToMember, _Mapping]] = ...) -> None: ...

class ToTeam(_message.Message):
    __slots__ = ("uuid", "data")
    UUID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    data: _member_pb2.Member
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., data: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class ToMember(_message.Message):
    __slots__ = ("uuid", "data")
    UUID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    data: _member_pb2.Member
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., data: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class ToInstallation(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ...) -> None: ...

class ToMachine(_message.Message):
    __slots__ = ("uuid",)
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ...) -> None: ...
