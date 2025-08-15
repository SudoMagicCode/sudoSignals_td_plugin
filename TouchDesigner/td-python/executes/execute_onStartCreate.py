# me - this DAT
#
# frame - the current frame
# state - True if the timeline is paused
#
# Make sure the corresponding toggle is enabled in the Execute DAT.

def start_up_client():
    parent.service.par.reinitextensions.pulse()
    parent.service.Signals_start_up()


def onStart():
    start_up_client()
    return


def onCreate():
    start_up_client()
    return


def onExit():
    parent.service.Clean_up()
    return


def onProjectPreSave():
    return


def onProjectPostSave():
    return
