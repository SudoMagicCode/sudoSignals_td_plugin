import signalsParACTIONS as ACTIONS

class ActionParser:
    '''
    '''
    def __init__(self, my_op:callable) -> None:
        self.My_op = my_op

    def Parse_par(self, par:callable) -> None:
        try:
            func = getattr(ACTIONS, par.name)
            func(par)
        except Exception as E:
            pass