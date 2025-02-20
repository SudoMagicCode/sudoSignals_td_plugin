from common import generic_pb2 as _generic_pb2
from common.enums import status_pb2 as _status_pb2
from common.options import message_options_pb2 as _message_options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountName(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ContactCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Contact
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Contact, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, Contact]
    def __init__(self, options: _Optional[_Mapping[str, Contact]] = ...) -> None: ...

class Contact(_message.Message):
    __slots__ = ("uuid", "contactState", "email", "sms", "web")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CONTACTSTATE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SMS_FIELD_NUMBER: _ClassVar[int]
    WEB_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    contactState: _status_pb2.ContactState
    email: EmailContact
    sms: SMSContact
    web: WebhookContact
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., contactState: _Optional[_Union[_status_pb2.ContactState, str]] = ..., email: _Optional[_Union[EmailContact, _Mapping]] = ..., sms: _Optional[_Union[SMSContact, _Mapping]] = ..., web: _Optional[_Union[WebhookContact, _Mapping]] = ...) -> None: ...

class EmailContact(_message.Message):
    __slots__ = ("handle",)
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    handle: str
    def __init__(self, handle: _Optional[str] = ...) -> None: ...

class SMSContact(_message.Message):
    __slots__ = ("handle",)
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    handle: str
    def __init__(self, handle: _Optional[str] = ...) -> None: ...

class WebhookContact(_message.Message):
    __slots__ = ("handle",)
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    handle: str
    def __init__(self, handle: _Optional[str] = ...) -> None: ...

class Connection(_message.Message):
    __slots__ = ("uuid", "handle")
    UUID_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    handle: _generic_pb2.ConnectionHandle
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., handle: _Optional[_Union[_generic_pb2.ConnectionHandle, _Mapping]] = ...) -> None: ...
