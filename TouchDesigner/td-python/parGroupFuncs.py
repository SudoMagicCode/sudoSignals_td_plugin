from google.protobuf import struct_pb2
import packets
import helperTypes

# A library of functions that return controls based on their par group style


def parGroupFloatFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Floats - will return controls for floats of all dimensions

    newMultiValue = packets.controls_fields.MultiValue(value={})    
    newMultiValueDefault = packets.controls_fields.MultiValue(value={})  
    newMultiMax = packets.controls_fields.MultiValue(value={})    
    newMultiMin = packets.controls_fields.MultiValue(value={})  
    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newMultiMin.value[index].number_value = parGroup.normMin[index]
            newMultiMax.value[index].number_value = parGroup.normMax[index]
            
            newMultiValue.value[index].number_value = parVal
            newMultiValueDefault.value[index].number_value = parGroup.default[index]

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    control.min_val.CopyFrom(newMultiMin)
    control.max_val.CopyFrom(newMultiMax)
    return control


def parGroupIntFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Ints - will return controls for ints of all dimensions
    newMultiValue = packets.controls_fields.MultiValue(value={})    
    newMultiValueDefault = packets.controls_fields.MultiValue(value={})  
    newMultiMax = packets.controls_fields.MultiValue(value={})    
    newMultiMin = packets.controls_fields.MultiValue(value={})  
    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:
            newMultiMin.value[index].number_value = parGroup.normMin[index]
            newMultiMax.value[index].number_value = parGroup.normMax[index]

            newMultiValue.value[index].number_value = parVal
            newMultiValueDefault.value[index].number_value = parGroup.default[index]

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    control.min_val.CopyFrom(newMultiMin)
    control.max_val.CopyFrom(newMultiMax)
    return control


def parGroupHeaderFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Header - will return controls for headers
    newMultiValue = packets.controls_fields.MultiValue(value={})    
    newMultiValueDefault = packets.controls_fields.MultiValue(value={})  
    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:

            newMultiValue.value[index].string_value = parVal
            newMultiValueDefault.value[index].string_value = parGroup.default[index] 

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    return control


def parGroupMenuFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Menu - returns menu objects that contain menu options (labels and names)

    newMultiValue = packets.controls_fields.MultiValue(value={})    
    newMultiValueDefault = packets.controls_fields.MultiValue(value={})  
    newMenuOptions = packets.controls_fields.MenuOptions(value={}) 

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:

            newMultiValue.value[index].string_value = parVal
            newMultiValueDefault.value[index].string_value = parGroup.default[index]

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
    newMultiValue = packets.controls_fields.MultiValue(value={})    
    newMultiValueDefault = packets.controls_fields.MultiValue(value={})  

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:

            newMultiValue.value[index].number_value = parVal
            newMultiValueDefault.value[index].number_value = parGroup.default[index]
    
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
    newMultiValue = packets.controls_fields.MultiValue(value={})    
    newMultiValueDefault = packets.controls_fields.MultiValue(value={})  

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:

            newMultiValue.value[index].string_value = parVal
            newMultiValueDefault.value[index].string_value = parGroup.default[index]

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    return control


def parGroupToggleFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Toggle - will return controls for toggle controls
    newMultiValue = packets.controls_fields.MultiValue(value={})    
    newMultiValueDefault = packets.controls_fields.MultiValue(value={})  

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:

            newMultiValue.value[index].bool_value = parVal
            newMultiValueDefault.value[index].bool_value = parGroup.default[index]

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    return control


def parGroupRGBFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Toggle - will return controls for toggle controls

    newMultiValue = packets.controls_fields.MultiValue(value={})    
    newMultiValueDefault = packets.controls_fields.MultiValue(value={})  
    newMultiMax = packets.controls_fields.MultiValue(value={})    
    newMultiMin = packets.controls_fields.MultiValue(value={})  

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:

            newMultiMin.value[index].number_value = parGroup.normMin[index]
            newMultiMax.value[index].number_value = parGroup.normMax[index]

            newMultiValue.value[index].number_value = parVal
            newMultiValueDefault.value[index].number_value = parGroup.default[index]

    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    control.min_val.CopyFrom(newMultiMin)
    control.max_val.CopyFrom(newMultiMax)
    return control


def parGroupRGBAFunc(control: packets.controls.Control, parGroup: helperTypes.parGroup) -> packets.controls.Control:
    # Par Group Toggle - will return controls for toggle controls

    newMultiValue = packets.controls_fields.MultiValue(value={})    
    newMultiValueDefault = packets.controls_fields.MultiValue(value={})  
    newMultiMax = packets.controls_fields.MultiValue(value={})    
    newMultiMin = packets.controls_fields.MultiValue(value={})  

    for index, parVal in enumerate(parGroup.val):
        if parVal is not None:

            newMultiMin.value[index].number_value = parGroup.normMin[index]
            newMultiMax.value[index].number_value = parGroup.normMax[index]

            newMultiValue.value[index].number_value = parVal
            newMultiValueDefault.value[index].number_value = parGroup.default[index]
            
    control.values.CopyFrom(newMultiValue)
    control.default_values.CopyFrom(newMultiValueDefault)
    control.min_val.CopyFrom(newMultiMin)
    control.max_val.CopyFrom(newMultiMax)
    return control
