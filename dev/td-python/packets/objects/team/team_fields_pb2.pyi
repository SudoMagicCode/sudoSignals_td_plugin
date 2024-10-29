from objects.team import member_pb2 as _member_pb2
from common.options import message_options_pb2 as _message_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MemberCollection(_message.Message):
    __slots__ = ("members",)
    class MembersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _member_pb2.Member
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.MessageMap[str, _member_pb2.Member]
    def __init__(self, members: _Optional[_Mapping[str, _member_pb2.Member]] = ...) -> None: ...

class InvitationCollection(_message.Message):
    __slots__ = ("invitations",)
    class InvitationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _member_pb2.Invitation
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_member_pb2.Invitation, _Mapping]] = ...) -> None: ...
    INVITATIONS_FIELD_NUMBER: _ClassVar[int]
    invitations: _containers.MessageMap[str, _member_pb2.Invitation]
    def __init__(self, invitations: _Optional[_Mapping[str, _member_pb2.Invitation]] = ...) -> None: ...
