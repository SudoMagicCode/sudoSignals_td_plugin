from common import generic_pb2 as _generic_pb2
from common.enums import controls_pb2 as _controls_pb2
from objects.controls import controls_fields_pb2 as _controls_fields_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Control(_message.Message):
    __slots__ = ("uuid", "control_type", "index", "label", "entity_reference", "min_val", "max_val", "values", "default_values", "menu_options")
    UUID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ENTITY_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    MIN_VAL_FIELD_NUMBER: _ClassVar[int]
    MAX_VAL_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUES_FIELD_NUMBER: _ClassVar[int]
    MENU_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    control_type: _controls_pb2.ControlType
    index: _controls_fields_pb2.ControlIndex
    label: _controls_fields_pb2.ControlLabel
    entity_reference: _generic_pb2.EntityReference
    min_val: _controls_fields_pb2.MultiValue
    max_val: _controls_fields_pb2.MultiValue
    values: _controls_fields_pb2.MultiValue
    default_values: _controls_fields_pb2.MultiValue
    menu_options: _controls_fields_pb2.MenuOptions
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., control_type: _Optional[_Union[_controls_pb2.ControlType, str]] = ..., index: _Optional[_Union[_controls_fields_pb2.ControlIndex, _Mapping]] = ..., label: _Optional[_Union[_controls_fields_pb2.ControlLabel, _Mapping]] = ..., entity_reference: _Optional[_Union[_generic_pb2.EntityReference, _Mapping]] = ..., min_val: _Optional[_Union[_controls_fields_pb2.MultiValue, _Mapping]] = ..., max_val: _Optional[_Union[_controls_fields_pb2.MultiValue, _Mapping]] = ..., values: _Optional[_Union[_controls_fields_pb2.MultiValue, _Mapping]] = ..., default_values: _Optional[_Union[_controls_fields_pb2.MultiValue, _Mapping]] = ..., menu_options: _Optional[_Union[_controls_fields_pb2.MenuOptions, _Mapping]] = ...) -> None: ...

class ControlCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Control
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Control, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, Control]
    def __init__(self, options: _Optional[_Mapping[str, Control]] = ...) -> None: ...

class ControlPage(_message.Message):
    __slots__ = ("uuid", "name", "controls")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    name: _generic_pb2.Name
    controls: ControlCollection
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., name: _Optional[_Union[_generic_pb2.Name, _Mapping]] = ..., controls: _Optional[_Union[ControlCollection, _Mapping]] = ...) -> None: ...

class ControlPageCollection(_message.Message):
    __slots__ = ("options",)
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ControlPage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ControlPage, _Mapping]] = ...) -> None: ...
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    options: _containers.MessageMap[str, ControlPage]
    def __init__(self, options: _Optional[_Mapping[str, ControlPage]] = ...) -> None: ...

class PromotedControl(_message.Message):
    __slots__ = ("uuid", "process_uuid", "control_page_uuid", "control_uuid", "entity_reference")
    UUID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_UUID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_PAGE_UUID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_UUID_FIELD_NUMBER: _ClassVar[int]
    ENTITY_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    uuid: _generic_pb2.Uuid
    process_uuid: _generic_pb2.Uuid
    control_page_uuid: _generic_pb2.Uuid
    control_uuid: _generic_pb2.Uuid
    entity_reference: _generic_pb2.EntityReference
    def __init__(self, uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., process_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., control_page_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., control_uuid: _Optional[_Union[_generic_pb2.Uuid, _Mapping]] = ..., entity_reference: _Optional[_Union[_generic_pb2.EntityReference, _Mapping]] = ...) -> None: ...
