from common import generic_pb2 as _generic_pb2
from common.enums import themes_pb2 as _themes_pb2
from objects.account import session_pb2 as _session_pb2
from objects.account import account_fields_pb2 as _account_fields_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ("uuid", "email", "name", "last_active", "preferred_theme", "last_path_visited", "contacts", "sessions")
    UUID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_THEME_FIELD_NUMBER: _ClassVar[int]
    LAST_PATH_VISITED_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    email: _generic_pb2.Email
    name: _account_fields_pb2.AccountName
    last_active: _timestamp_pb2.Timestamp
    preferred_theme: _themes_pb2.AccountTheme
    last_path_visited: _generic_pb2.UrlPath
    contacts: _account_fields_pb2.ContactCollection
    sessions: _session_pb2.SessionCollection
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., email: _Optional[_Union[_generic_pb2.Email, _Mapping]] = ..., name: _Optional[_Union[_account_fields_pb2.AccountName, _Mapping]] = ..., last_active: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., preferred_theme: _Optional[_Union[_themes_pb2.AccountTheme, str]] = ..., last_path_visited: _Optional[_Union[_generic_pb2.UrlPath, _Mapping]] = ..., contacts: _Optional[_Union[_account_fields_pb2.ContactCollection, _Mapping]] = ..., sessions: _Optional[_Union[_session_pb2.SessionCollection, _Mapping]] = ...) -> None: ...
