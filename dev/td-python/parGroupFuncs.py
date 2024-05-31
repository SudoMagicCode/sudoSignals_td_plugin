from google.protobuf import struct_pb2
import packets
import helperTypes

# A library of functions that return controls based on their par group style


def parGroupFloatFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Par Group Floats - will return controls for floats of all dimensions

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newMin = struct_pb2.Value()
            newMax = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.number_value = parVal
            newMin.number_value = parGroup.normMin[index]
            newMax.number_value = parGroup.normMax[index]
            newDefault.number_value = parGroup.default[index]
            control.minVal.append(newMin)
            control.maxVal.append(newMax)

            control.values.append(newValue)
            control.defaultValues.append(newDefault)

    return control


def parGroupIntFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Par Group Ints - will return controls for ints of all dimensions

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newMin = struct_pb2.Value()
            newMax = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.number_value = parVal
            newMin.number_value = parGroup.normMin[index]
            newMax.number_value = parGroup.normMax[index]
            newDefault.number_value = parGroup.default[index]
            control.minVal.append(newMin)
            control.maxVal.append(newMax)

            control.values.append(newValue)
            control.defaultValues.append(newDefault)
    return control


def parGroupHeaderFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Par Group Header - will return controls for headers

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.string_value = parVal
            newDefault.string_value = parGroup.default[index]

            control.values.append(newValue)
            control.defaultValues.append(newDefault)
    return control


def parGroupMenuFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Par Group Menu - returns menu objects that contain menu options (labels and names)

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.string_value = parVal
            newDefault.string_value = parGroup.default[index]

            control.values.append(newValue)
            control.defaultValues.append(newDefault)

        parLabels = parGroup.menuLabels[index]
        parNames = parGroup.menuNames[index]

        for eachIndex, eachLabel in enumerate(parLabels):
            control.menuOptions[eachLabel] = parNames[eachIndex]

    return control


def parGroupMomentaryFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Not yet completed

    return control


def parGroupPulseFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Par Group Pulse - will return controls for pulse controls

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.number_value = parVal
            newDefault.number_value = parGroup.default[index]

            control.values.append(newValue)
            control.defaultValues.append(newDefault)
    return control


def parGroupPythonFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Not yet completed

    return control


def parGroupSequenceFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Not yet completed

    return control


def parGroupStringFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Par Group String - will return controls for string controls

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.string_value = parVal
            newDefault.string_value = parGroup.default[index]

            control.values.append(newValue)
            control.defaultValues.append(newDefault)
    return control


def parGroupToggleFunc(control: packets.fieldTypes_pb2.Control, parGroup: helperTypes.parGroup) -> packets.fieldTypes_pb2.Control:
    # Par Group Toggle - will return controls for toggle controls

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.bool_value = parVal
            newDefault.bool_value = parGroup.default[index]

            control.values.append(newValue)
            control.defaultValues.append(newDefault)
    return control
