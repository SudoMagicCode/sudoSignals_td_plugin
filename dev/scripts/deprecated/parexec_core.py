# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

extOp = op('base_private_ext')

def onValueChange(par, prev):
	print(par)
	# use par.eval() to get current value

	return

def onPulse(par):
	if par.name == 'Setdev':
		extOp.SetDev()
	
	elif par.name == 'Setprod':
		extOp.SetProd()

	return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
	