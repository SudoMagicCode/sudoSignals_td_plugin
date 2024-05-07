from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DynamoRecord(_message.Message):
    __slots__ = ("PartitionKey", "SortKey", "RecordType", "RecordTypeLookup", "TTL")
    PARTITIONKEY_FIELD_NUMBER: _ClassVar[int]
    SORTKEY_FIELD_NUMBER: _ClassVar[int]
    RECORDTYPE_FIELD_NUMBER: _ClassVar[int]
    RECORDTYPELOOKUP_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    PartitionKey: str
    SortKey: str
    RecordType: str
    RecordTypeLookup: str
    TTL: int
    def __init__(self, PartitionKey: _Optional[str] = ..., SortKey: _Optional[str] = ..., RecordType: _Optional[str] = ..., RecordTypeLookup: _Optional[str] = ..., TTL: _Optional[int] = ...) -> None: ...
