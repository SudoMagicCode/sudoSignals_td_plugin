# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

def onValueChange(par, prev):
	# use par.eval() to get current value
	if par.name == 'Productid':
		print("Product ID Changed")
		op('base_private_ext').ProductId = par.eval()

	elif par.name == 'Controlcomp':
		op('base_private_ext').ControlComp = par.eval()
	return
	
def onPulse(par):
	op('base_private_ext').PulsePar(par.name)
	return