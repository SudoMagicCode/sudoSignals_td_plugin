from google.protobuf import any_pb2 as _any_pb2
from common.enums import subscriptions_pb2 as _subscriptions_pb2
from common import generic_pb2 as _generic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PublisherPayload(_message.Message):
    __slots__ = ("newImage", "oldImage", "eventName", "PartitionKey", "SortKey")
    NEWIMAGE_FIELD_NUMBER: _ClassVar[int]
    OLDIMAGE_FIELD_NUMBER: _ClassVar[int]
    EVENTNAME_FIELD_NUMBER: _ClassVar[int]
    PARTITIONKEY_FIELD_NUMBER: _ClassVar[int]
    SORTKEY_FIELD_NUMBER: _ClassVar[int]
    newImage: _any_pb2.Any
    oldImage: _any_pb2.Any
    eventName: str
    PartitionKey: str
    SortKey: str
    def __init__(self, newImage: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., oldImage: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., eventName: _Optional[str] = ..., PartitionKey: _Optional[str] = ..., SortKey: _Optional[str] = ...) -> None: ...

class SubscriptionPayload(_message.Message):
    __slots__ = ("uuid", "subscriptionType", "objectUuid", "mask")
    UUID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECTUUID_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    subscriptionType: _subscriptions_pb2.SubscriptionTypes
    objectUuid: _generic_pb2.Uuid
    mask: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., subscriptionType: _Optional[_Union[_subscriptions_pb2.SubscriptionTypes, str]] = ..., objectUuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., mask: _Optional[_Iterable[str]] = ...) -> None: ...
