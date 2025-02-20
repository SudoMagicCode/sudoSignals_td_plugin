# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev) -> None:
    op('base_private_ext').Parse_par(par)
    return
    
def onPulse(par) -> None:
    op('base_private_ext').Parse_par(par)
    return

