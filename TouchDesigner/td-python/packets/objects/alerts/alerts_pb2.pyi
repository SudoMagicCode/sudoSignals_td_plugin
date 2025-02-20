from common import generic_pb2 as _generic_pb2
from common.enums import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AlertRuleCollection(_message.Message):
    __slots__ = ("rules",)
    class RulesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: AlertRule
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[AlertRule, _Mapping]] = ...) -> None: ...
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.MessageMap[str, AlertRule]
    def __init__(self, rules: _Optional[_Mapping[str, AlertRule]] = ...) -> None: ...

class AlertRule(_message.Message):
    __slots__ = ("uuid", "account_uuid", "object_uuid", "contact_uuid", "state_rule")
    UUID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_UUID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_UUID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_UUID_FIELD_NUMBER: _ClassVar[int]
    STATE_RULE_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    account_uuid: _generic_pb2.Uuid
    object_uuid: _generic_pb2.Uuid
    contact_uuid: _generic_pb2.Uuid
    state_rule: StateRule
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., account_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., object_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., contact_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., state_rule: _Optional[_Union[StateRule, _Mapping]] = ...) -> None: ...

class StateRule(_message.Message):
    __slots__ = ("alert_level",)
    ALERT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    alert_level: _status_pb2.Status
    def __init__(self, alert_level: _Optional[_Union[_status_pb2.Status, str]] = ...) -> None: ...
