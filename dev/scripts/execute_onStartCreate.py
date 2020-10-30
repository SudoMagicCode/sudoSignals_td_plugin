# me - this DAT
# 
# frame - the current frame
# state - True if the timeline is paused
# 
# Make sure the corresponding toggle is enabled in the Execute DAT.

def onStart():
	op('base_private_ext').par.reinitextensions.pulse()
	return

def onCreate():
	op('base_private_ext').par.reinitextensions.pulse()
	return

def onExit():
	return

def onProjectPreSave():
	return

def onProjectPostSave():
	return

	