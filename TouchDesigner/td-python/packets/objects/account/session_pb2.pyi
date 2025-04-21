from common import generic_pb2 as _generic_pb2
from common.enums import subscriptions_pb2 as _subscriptions_pb2
from common.options import message_options_pb2 as _message_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subscription(_message.Message):
    __slots__ = ("uuid", "handle", "token", "account_uuid", "subscription_type", "connection_uuid", "object_uuid", "mask")
    UUID_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_UUID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_UUID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_UUID_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    handle: _generic_pb2.ConnectionHandle
    token: _generic_pb2.Token
    account_uuid: _generic_pb2.Uuid
    subscription_type: _subscriptions_pb2.SubscriptionTypes
    connection_uuid: _generic_pb2.Uuid
    object_uuid: _generic_pb2.Uuid
    mask: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., handle: _Optional[_Union[_generic_pb2.ConnectionHandle, _Mapping]] = ..., token: _Optional[_Union[_generic_pb2.Token, _Mapping]] = ..., account_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., subscription_type: _Optional[_Union[_subscriptions_pb2.SubscriptionTypes, str]] = ..., connection_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., object_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., mask: _Optional[_Iterable[str]] = ...) -> None: ...

class SubscriptionCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Subscription
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Subscription, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, Subscription]
    def __init__(self, options: _Optional[_Mapping[str, Subscription]] = ...) -> None: ...

class SessionCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Session
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Session, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, Session]
    def __init__(self, options: _Optional[_Mapping[str, Session]] = ...) -> None: ...

class Session(_message.Message):
    __slots__ = ("uuid", "handle", "subscriptions")
    UUID_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    handle: _generic_pb2.ConnectionHandle
    subscriptions: SubscriptionCollection
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., handle: _Optional[_Union[_generic_pb2.ConnectionHandle, _Mapping]] = ..., subscriptions: _Optional[_Union[SubscriptionCollection, _Mapping]] = ...) -> None: ...
