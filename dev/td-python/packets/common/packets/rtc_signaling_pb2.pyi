from google.protobuf import any_pb2 as _any_pb2
from common.enums import packets_pb2 as _packets_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SignalingPacket(_message.Message):
    __slots__ = ("action", "channel", "data", "target")
    class OfferData(_message.Message):
        __slots__ = ("type", "sdp")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SDP_FIELD_NUMBER: _ClassVar[int]
        type: str
        sdp: str
        def __init__(self, type: _Optional[str] = ..., sdp: _Optional[str] = ...) -> None: ...
    class AnswerData(_message.Message):
        __slots__ = ("type", "sdp")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SDP_FIELD_NUMBER: _ClassVar[int]
        type: str
        sdp: str
        def __init__(self, type: _Optional[str] = ..., sdp: _Optional[str] = ...) -> None: ...
    class IceCandidateData(_message.Message):
        __slots__ = ("candidate", "sdpMLineIndex", "sdpMid")
        CANDIDATE_FIELD_NUMBER: _ClassVar[int]
        SDPMLINEINDEX_FIELD_NUMBER: _ClassVar[int]
        SDPMID_FIELD_NUMBER: _ClassVar[int]
        candidate: str
        sdpMLineIndex: int
        sdpMid: str
        def __init__(self, candidate: _Optional[str] = ..., sdpMLineIndex: _Optional[int] = ..., sdpMid: _Optional[str] = ...) -> None: ...
    class GatherData(_message.Message):
        __slots__ = ("activeOffers",)
        ACTIVEOFFERS_FIELD_NUMBER: _ClassVar[int]
        activeOffers: _containers.RepeatedCompositeFieldContainer[SignalingPacket.OfferData]
        def __init__(self, activeOffers: _Optional[_Iterable[_Union[SignalingPacket.OfferData, _Mapping]]] = ...) -> None: ...
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    action: _packets_pb2.SignalingPacketType
    channel: str
    data: _any_pb2.Any
    target: str
    def __init__(self, action: _Optional[_Union[_packets_pb2.SignalingPacketType, str]] = ..., channel: _Optional[str] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., target: _Optional[str] = ..., **kwargs) -> None: ...
