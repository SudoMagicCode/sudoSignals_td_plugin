from common import generic_pb2 as _generic_pb2
from objects.access_code import access_code_fields_pb2 as _access_code_fields_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTeamRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: _generic_pb2.Name
    def __init__(self, name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ...) -> None: ...

class CreateInstallationRequest(_message.Message):
    __slots__ = ("name", "team_uuid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEAM_UUID_FIELD_NUMBER: _ClassVar[int]
    name: _generic_pb2.Name
    team_uuid: _generic_pb2.Uuid
    def __init__(self, name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ..., team_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ...) -> None: ...

class CreateMachineRequest(_message.Message):
    __slots__ = ("name", "code", "team_uuid", "installation_uuid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TEAM_UUID_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_UUID_FIELD_NUMBER: _ClassVar[int]
    name: _generic_pb2.Name
    code: _access_code_fields_pb2.Code
    team_uuid: _generic_pb2.Uuid
    installation_uuid: _generic_pb2.Uuid
    def __init__(self, name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ..., code: _Optional[_Union[_access_code_fields_pb2.Code, _Mapping]] = ..., team_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., installation_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ...) -> None: ...
