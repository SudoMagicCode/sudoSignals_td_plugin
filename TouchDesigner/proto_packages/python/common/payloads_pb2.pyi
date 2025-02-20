from common import fieldTypes_pb2 as _fieldTypes_pb2
from common import signalsEnums_pb2 as _signalsEnums_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class ConnectionPayload(_message.Message):
    __slots__ = ("accountUuid", "connectionToken")
    ACCOUNTUUID_FIELD_NUMBER: _ClassVar[int]
    CONNECTIONTOKEN_FIELD_NUMBER: _ClassVar[int]
    accountUuid: str
    connectionToken: str
    def __init__(self, accountUuid: _Optional[str] = ..., connectionToken: _Optional[str] = ...) -> None: ...

class SubscriptionPayload(_message.Message):
    __slots__ = ("uuid", "subscriptionType", "objectUuid", "mask")
    UUID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECTUUID_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    subscriptionType: _signalsEnums_pb2.SubscriptionTypes
    objectUuid: str
    mask: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid: _Optional[str] = ..., subscriptionType: _Optional[_Union[_signalsEnums_pb2.SubscriptionTypes, str]] = ..., objectUuid: _Optional[str] = ..., mask: _Optional[_Iterable[str]] = ...) -> None: ...

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

class ProcessPayload(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class RpcPayload(_message.Message):
    __slots__ = ("request", "response", "data")
    class RequestEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ResponseEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    request: _containers.ScalarMap[str, str]
    response: _containers.ScalarMap[str, str]
    data: _any_pb2.Any
    def __init__(self, request: _Optional[_Mapping[str, str]] = ..., response: _Optional[_Mapping[str, str]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class ProcessLogPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProcessReportPayload(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProcessControlPayload(_message.Message):
    __slots__ = ("data",)
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _fieldTypes_pb2.ControlPage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_fieldTypes_pb2.ControlPage, _Mapping]] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: _containers.MessageMap[str, _fieldTypes_pb2.ControlPage]
    def __init__(self, data: _Optional[_Mapping[str, _fieldTypes_pb2.ControlPage]] = ...) -> None: ...

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
    action: _signalsEnums_pb2.MachineActions
    data: _containers.ScalarMap[str, str]
    def __init__(self, action: _Optional[_Union[_signalsEnums_pb2.MachineActions, str]] = ..., data: _Optional[_Mapping[str, str]] = ...) -> None: ...

class AlertPayload(_message.Message):
    __slots__ = ("objectName", "timeReported", "alertingCondition")
    OBJECTNAME_FIELD_NUMBER: _ClassVar[int]
    TIMEREPORTED_FIELD_NUMBER: _ClassVar[int]
    ALERTINGCONDITION_FIELD_NUMBER: _ClassVar[int]
    objectName: str
    timeReported: str
    alertingCondition: str
    def __init__(self, objectName: _Optional[str] = ..., timeReported: _Optional[str] = ..., alertingCondition: _Optional[str] = ...) -> None: ...

class RTCPayload(_message.Message):
    __slots__ = ("connectionHandle", "identifier", "offer", "answer", "iceCandidate")
    CONNECTIONHANDLE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    ICECANDIDATE_FIELD_NUMBER: _ClassVar[int]
    connectionHandle: str
    identifier: str
    offer: OfferPayload
    answer: AnswerPayload
    iceCandidate: ICEPayload
    def __init__(self, connectionHandle: _Optional[str] = ..., identifier: _Optional[str] = ..., offer: _Optional[_Union[OfferPayload, _Mapping]] = ..., answer: _Optional[_Union[AnswerPayload, _Mapping]] = ..., iceCandidate: _Optional[_Union[ICEPayload, _Mapping]] = ...) -> None: ...

class OfferPayload(_message.Message):
    __slots__ = ("sdp",)
    SDP_FIELD_NUMBER: _ClassVar[int]
    sdp: str
    def __init__(self, sdp: _Optional[str] = ...) -> None: ...

class AnswerPayload(_message.Message):
    __slots__ = ("sdp",)
    SDP_FIELD_NUMBER: _ClassVar[int]
    sdp: str
    def __init__(self, sdp: _Optional[str] = ...) -> None: ...

class ICEPayload(_message.Message):
    __slots__ = ("candidate", "SDPMid", "SDPMLineIndex", "UsernameFragment")
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    SDPMID_FIELD_NUMBER: _ClassVar[int]
    SDPMLINEINDEX_FIELD_NUMBER: _ClassVar[int]
    USERNAMEFRAGMENT_FIELD_NUMBER: _ClassVar[int]
    candidate: str
    SDPMid: str
    SDPMLineIndex: int
    UsernameFragment: str
    def __init__(self, candidate: _Optional[str] = ..., SDPMid: _Optional[str] = ..., SDPMLineIndex: _Optional[int] = ..., UsernameFragment: _Optional[str] = ...) -> None: ...
