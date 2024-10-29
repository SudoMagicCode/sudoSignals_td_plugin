from google.protobuf import struct_pb2
import packets
import helperTypes

# A library of functions that return controls based on their par group style


def parGroupFloatFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Floats - will return controls for floats of all dimensions

    newMultiValue = packets.controls_fields.MultiValue(value=[])    
    newMultiValueDefault = packets.controls_fields.MultiValue(value=[])  
    newMultiMax = packets.controls_fields.MultiValue(value=[])    
    newMultiMin = packets.controls_fields.MultiValue(value=[])  
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
            newMultiMin.value.append(newMin)
            newMultiMax.value.append(newMax)

            newMultiValue.value.append(newValue)
            newMultiValueDefault.value.append(newDefault)

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    control.min_val.CopyFrom(newMultiMin)
    control.max_val.CopyFrom(newMultiMax)
    return control


def parGroupIntFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Ints - will return controls for ints of all dimensions
    newMultiValue = packets.controls_fields.MultiValue(value=[])    
    newMultiValueDefault = packets.controls_fields.MultiValue(value=[])  
    newMultiMax = packets.controls_fields.MultiValue(value=[])    
    newMultiMin = packets.controls_fields.MultiValue(value=[])  
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
            newMultiMin.value.append(newMin)
            newMultiMax.value.append(newMax)

            newMultiValue.value.append(newValue)
            newMultiValueDefault.value.append(newDefault)

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    control.min_val.CopyFrom(newMultiMin)
    control.max_val.CopyFrom(newMultiMax)
    return control


def parGroupHeaderFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Header - will return controls for headers
    newMultiValue = packets.controls_fields.MultiValue(value=[])    
    newMultiValueDefault = packets.controls_fields.MultiValue(value=[])  
    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.string_value = parVal
            newDefault.string_value = parGroup.default[index]  

            newMultiValue.value.append(newValue)
            newMultiValueDefault.value.append(newDefault)

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    return control


def parGroupMenuFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Menu - returns menu objects that contain menu options (labels and names)

    newMultiValue = packets.controls_fields.MultiValue(value=[])    
    newMultiValueDefault = packets.controls_fields.MultiValue(value=[])  
    newMenuOptions = packets.controls_fields.MenuOptions(value={}) 

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.string_value = parVal
            newDefault.string_value = parGroup.default[index]

            newMultiValue.value.append(newValue)
            newMultiValueDefault.value.append(newDefault)

        parLabels = parGroup.menuLabels[index]
        parNames = parGroup.menuNames[index]

        for eachIndex, eachName in enumerate(parNames):
            newMenuOptions.value[eachName] = parLabels[eachIndex]
    
    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    control.menu_options.CopyFrom(newMenuOptions)
    return control


def parGroupMomentaryFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Not yet completed

    return control


def parGroupPulseFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Pulse - will return controls for pulse controls
    newMultiValue = packets.controls_fields.MultiValue(value=[])    
    newMultiValueDefault = packets.controls_fields.MultiValue(value=[])  

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.number_value = parVal
            newDefault.number_value = parGroup.default[index]

            newMultiValue.value.append(newValue)
            newMultiValueDefault.value.append(newDefault)
    
    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    return control


def parGroupPythonFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Not yet completed

    return control


def parGroupSequenceFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Not yet completed

    return control


def parGroupStringFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group String - will return controls for string controls
    newMultiValue = packets.controls_fields.MultiValue(value=[])    
    newMultiValueDefault = packets.controls_fields.MultiValue(value=[])  

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.string_value = parVal
            newDefault.string_value = parGroup.default[index]

            newMultiValue.value.append(newValue)
            newMultiValueDefault.value.append(newDefault)

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    return control


def parGroupToggleFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Toggle - will return controls for toggle controls
    newMultiValue = packets.controls_fields.MultiValue(value=[])    
    newMultiValueDefault = packets.controls_fields.MultiValue(value=[])  

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newValue = struct_pb2.Value()
            newDefault = struct_pb2.Value()

            newValue.bool_value = parVal
            newDefault.bool_value = parGroup.default[index]

            newMultiValue.value.append(newValue)
            newMultiValueDefault.value.append(newDefault)

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    return control


def parGroupRGBFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Toggle - will return controls for toggle controls

    newMultiValue = packets.controls_fields.MultiValue(value=[])    
    newMultiValueDefault = packets.controls_fields.MultiValue(value=[])  
    newMultiMax = packets.controls_fields.MultiValue(value=[])    
    newMultiMin = packets.controls_fields.MultiValue(value=[])  

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
            newMultiMin.value.append(newMin)
            newMultiMax.value.append(newMax)

            newMultiValue.value.append(newValue)
            newMultiValueDefault.value.append(newDefault)

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    control.min_val.CopyFrom(newMultiMin)
    control.max_val.CopyFrom(newMultiMax)
    return control


def parGroupRGBAFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Toggle - will return controls for toggle controls

    newMultiValue = packets.controls_fields.MultiValue(value=[])    
    newMultiValueDefault = packets.controls_fields.MultiValue(value=[])  
    newMultiMax = packets.controls_fields.MultiValue(value=[])    
    newMultiMin = packets.controls_fields.MultiValue(value=[])  

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
            newMultiMin.value.append(newMin)
            newMultiMax.value.append(newMax)

            newMultiValue.value.append(newValue)
            newMultiValueDefault.value.append(newDefault)
            
    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    control.min_val.CopyFrom(newMultiMin)
    control.max_val.CopyFrom(newMultiMax)
    return control
