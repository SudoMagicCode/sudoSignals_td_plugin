from common import generic_pb2 as _generic_pb2
from common.enums import roles_pb2 as _roles_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Member(_message.Message):
    __slots__ = ("uuid", "role", "date_added", "last_active", "email", "name", "last_path_visited")
    UUID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    DATE_ADDED_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_PATH_VISITED_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    role: _roles_pb2.Role
    date_added: _timestamp_pb2.Timestamp
    last_active: _timestamp_pb2.Timestamp
    email: _generic_pb2.Email
    name: _generic_pb2.Name
    last_path_visited: _generic_pb2.UrlPath
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., role: _Optional[_Union[_roles_pb2.Role, str]] = ..., date_added: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_active: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., email: _Optional[_Union[_generic_pb2.Email, _Mapping]] = ..., name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ..., last_path_visited: _Optional[_Union[_generic_pb2.UrlPath, _Mapping]] = ...) -> None: ...

class Invitation(_message.Message):
    __slots__ = ("email", "role", "date_sent")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    DATE_SENT_FIELD_NUMBER: _ClassVar[int]
    email: _generic_pb2.Email
    role: _roles_pb2.Role
    date_sent: _timestamp_pb2.Timestamp
    def __init__(self, email: _Optional[_Union[_generic_pb2.Email, _Mapping]] = ..., role: _Optional[_Union[_roles_pb2.Role, str]] = ..., date_sent: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
