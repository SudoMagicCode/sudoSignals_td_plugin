from objects.profile import profile_pb2 as _profile_pb2
from common.enums import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccessPayload(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class SourcePayload(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class MachineControlPayload(_message.Message):
    __slots__ = ("action", "data")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    action: _actions_pb2.MachineActions
    data: _containers.ScalarMap[str, str]
    def __init__(self, action: _Optional[_Union[_actions_pb2.MachineActions, str]] = ..., data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ProfilePayload(_message.Message):
    __slots__ = ("active", "availableProfiles", "isDirty")
    class AvailableProfilesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _profile_pb2.Profile
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_profile_pb2.Profile, _Mapping]] = ...) -> None: ...
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLEPROFILES_FIELD_NUMBER: _ClassVar[int]
    ISDIRTY_FIELD_NUMBER: _ClassVar[int]
    active: _profile_pb2.Profile
    availableProfiles: _containers.MessageMap[str, _profile_pb2.Profile]
    isDirty: bool
    def __init__(self, active: _Optional[_Union[_profile_pb2.Profile, _Mapping]] = ..., availableProfiles: _Optional[_Mapping[str, _profile_pb2.Profile]] = ..., isDirty: bool = ...) -> None: ...
