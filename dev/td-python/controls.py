import utils
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
            newControlPage = packets.controls.ControlPage()
            newControlPage.name.CopyFrom(packets.generic.Name(value=p.name))
            newControlPage.uuid.CopyFrom(packets.generic.Uuid(value=p.owner.path+"#"+str(idx)))

            newControls = utils.CreateAllParDataBlocks(p)
            for k, v in newControls.items():
                newControlPage.controls.options[k].CopyFrom(v)
            controlPages.append(newControlPage)
        return controlPages

    def UpdateControlComp(self, state: packets.controls.Control) -> None:
        path_to_control_tox = state.entity_reference.value["path"]
        par_name = state.entity_reference.value["name"]
        control_style = state.control_type
        control_values = state.values

        match control_style:
            case packets.control_enums.CONTROL_PULSE:
                op(path_to_control_tox).parGroup[par_name].pulse()

            case packets.control_enums.CONTROL_INT:
                my_int_values = [
                   control_values.value[idx].number_value for idx in control_values.value]
                op(path_to_control_tox).parGroup[par_name] = my_int_values

            case packets.control_enums.CONTROL_FLOAT:
                my_int_values = [
                    control_values.value[idx].number_value for idx in control_values.value]
                op(path_to_control_tox).parGroup[par_name] = my_int_values

            case packets.control_enums.CONTROL_COLOR:
                my_int_values = [
                    control_values.value[idx].number_value for idx in control_values.value]
                op(path_to_control_tox).parGroup[par_name] = my_int_values

            case packets.control_enums.CONTROL_MENU:
                op(path_to_control_tox).parGroup[par_name] = control_values.value[0].string_value

            case packets.control_enums.CONTROL_TOGGLE:
                op(path_to_control_tox).parGroup[par_name] = control_values.value[0].bool_value

            case packets.control_enums.CONTROL_STRING:
                op(path_to_control_tox).parGroup[par_name] = control_values.value[0].string_value

            case _:
                print(f"{control_style} control type is not yet supported")
