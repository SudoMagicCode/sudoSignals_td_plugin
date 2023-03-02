from __future__ import annotations

try: 
    import signalsTDPluginEXT
except:
    pass

# type hinting used for code completion
SIGNALS:signalsTDPluginEXT.SignalsClient = op('base_private_ext')

def Signalsid(par) -> None:
    pass

def Signalsname(par) -> None:
    pass

def Connected(par) -> None:
    pass

def Controlcomp(par) -> None:
    SIGNALS.ControlComp = par.eval()
    SIGNALS.SetControls()

def Customreports(par) -> None:
    pass

#NOTE Advanced Settings

def Startupdelay(par) -> None:
    pass

def Resetconnection(par) -> None:
    SIGNALS.par.reinitextensions.pulse()
    SIGNALS.SignalsStartUp()

#NOTE About Page
def Help(par) -> None:
    webLink = SIGNALS.LINKS.get('Help')
    ui.viewFile(webLink)

def Sudosignalsdashboard(par) -> None:
    webLink = SIGNALS.LINKS.get('Sudosignalsdashboard')
    ui.viewFile(webLink)

def Forum(par) -> None:
    webLink = SIGNALS.LINKS.get('Forum')
    ui.viewFile(webLink)

def Bugreport(par) -> None:
    webLink = SIGNALS.LINKS.get('Bugreport')
    ui.viewFile(webLink)
