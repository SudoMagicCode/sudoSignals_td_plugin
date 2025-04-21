from common.enums import themes_pb2 as _themes_pb2
from objects.profile import profile_pb2 as _profile_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class File_ClientSettings(_message.Message):
    __slots__ = ("pluginPort", "profileDirectory", "logDirectory", "theme")
    PLUGINPORT_FIELD_NUMBER: _ClassVar[int]
    PROFILEDIRECTORY_FIELD_NUMBER: _ClassVar[int]
    LOGDIRECTORY_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    pluginPort: int
    profileDirectory: str
    logDirectory: str
    theme: _themes_pb2.AccountTheme
    def __init__(self, pluginPort: _Optional[int] = ..., profileDirectory: _Optional[str] = ..., logDirectory: _Optional[str] = ..., theme: _Optional[_Union[_themes_pb2.AccountTheme, str]] = ...) -> None: ...

class File_Profile(_message.Message):
    __slots__ = ("profile",)
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    profile: _profile_pb2.Profile
    def __init__(self, profile: _Optional[_Union[_profile_pb2.Profile, _Mapping]] = ...) -> None: ...

class File_Token(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
