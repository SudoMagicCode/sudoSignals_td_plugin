from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOG_LOG: _ClassVar[LogLevel]
    LOG_INFO: _ClassVar[LogLevel]
    LOG_WARN: _ClassVar[LogLevel]
    LOG_CRIT: _ClassVar[LogLevel]
    LOG_ALERT: _ClassVar[LogLevel]
LOG_LOG: LogLevel
LOG_INFO: LogLevel
LOG_WARN: LogLevel
LOG_CRIT: LogLevel
LOG_ALERT: LogLevel
