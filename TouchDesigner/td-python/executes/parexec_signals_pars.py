# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev) -> None:
    parent.service.Parse_par(par)
    return
    
def onPulse(par) -> None:
    parent.service.Parse_par(par)
    return

