from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MachineActions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED_MACHINE_ACTION: _ClassVar[MachineActions]
    START_ALL_PROCESSES: _ClassVar[MachineActions]
    STOP_ALL_PROCESSES: _ClassVar[MachineActions]
    RESTART_MACHINE: _ClassVar[MachineActions]
    CHANGE_PROFILE: _ClassVar[MachineActions]
    START_PROCESS: _ClassVar[MachineActions]
    STOP_PROCESS: _ClassVar[MachineActions]
    RESTART_PROCESS: _ClassVar[MachineActions]
UNDEFINED_MACHINE_ACTION: MachineActions
START_ALL_PROCESSES: MachineActions
STOP_ALL_PROCESSES: MachineActions
RESTART_MACHINE: MachineActions
CHANGE_PROFILE: MachineActions
START_PROCESS: MachineActions
STOP_PROCESS: MachineActions
RESTART_PROCESS: MachineActions
