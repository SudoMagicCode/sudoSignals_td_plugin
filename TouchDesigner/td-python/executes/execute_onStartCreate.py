# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def onStart():
	parent.service.par.reinitextensions.pulse()
	parent.service.SignalsStartUp()
	
	return

def onCreate():
	parent.service.par.reinitextensions.pulse()
	parent.service.SignalsStartUp()
	return

def onExit():
	parent.service.Clean_up()
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return

	