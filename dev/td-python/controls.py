
import utils
import signalsErrors
import packets


class SignalsControls:
    def __init__(self, op: OP) -> None:
        self._controllable = op
        return

    @property
    def ControlComp(self) -> callable:
        return self._controllable

    @ControlComp.setter
    def ControlComp(self, op):
        self._controllable = op

    def CreateControls(self) -> list:
        controlPages = []
        pagesToSend = self._controllable.customPages

        for idx, p in enumerate(pagesToSend):
            newControlPage = packets.fieldTypes_pb2.ControlPage()
            newControlPage.name = p.name
            newControlPage.uuid = p.owner.path+"#"+str(idx)

            newControls = utils.CreateAllParDataBlocks(p)
            for k, v in newControls.items():
                newControlPage.controls[k].CopyFrom(v)
            controlPages.append(newControlPage)
        return controlPages

    def UpdateControlComp(self, state: packets.fieldTypes_pb2.Control) -> None:
        path_to_control_tox = state.entityReference["path"]
        par_name = state.entityReference["name"]
        control_style = state.controlType
        control_values = state.values

        match control_style:
            case packets.signalsEnums_pb2.CONTROL_PULSE:
                op(path_to_control_tox).parGroup[par_name].pulse()
            case packets.signalsEnums_pb2.CONTROL_INT:
                my_int_values = [
                    value.number_value for value in control_values]
                op(path_to_control_tox).parGroup[par_name] = my_int_values
            case packets.signalsEnums_pb2.CONTROL_FLOAT:
                my_int_values = [
                    value.number_value for value in control_values]
                op(path_to_control_tox).parGroup[par_name] = my_int_values
            case packets.signalsEnums_pb2.CONTROL_MENU:
                op(path_to_control_tox).parGroup[par_name] = control_values[0].string_value
            case packets.signalsEnums_pb2.CONTROL_TOGGLE:
                op(path_to_control_tox).parGroup[par_name] = control_values[0].bool_value
            case packets.signalsEnums_pb2.CONTROL_STRING:
                op(path_to_control_tox).parGroup[par_name] = control_values[0].string_value
            case _:
                print(f"{control_style} control type is not yet supported")
