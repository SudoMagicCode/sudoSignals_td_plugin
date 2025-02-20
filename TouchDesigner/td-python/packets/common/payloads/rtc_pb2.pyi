from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
