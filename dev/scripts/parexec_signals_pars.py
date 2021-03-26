# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):

	if par.name == 'Controlcomp':
		op('base_private_ext').ext.Signals.ControlComp = par.eval()
		op('base_private_ext').ext.Signals.SetControls()

	return
	
def onPulse(par):
	
	if par.page == 'About':
		op('base_private_ext').PulsePar(par)
	return