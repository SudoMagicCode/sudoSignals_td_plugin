# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

import signalsParACTIONS as ACTIONS

def onValueChange(par, prev) -> None:
    ParsePar(par)

    return
    
def onPulse(par) -> None:
    ParsePar(par)

    return

def ParsePar(par:callable) -> callable:
    try:
        func = getattr(ACTIONS, par.name)
        func(par)
    except Exception as E:
        pass
        
    return
