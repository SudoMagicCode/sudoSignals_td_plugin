from __future__ import annotations

try: 
    import signalsTDPluginEXT
except:
    pass

# type hinting used for code completion
SIGNALS:signalsTDPluginEXT.SignalsClient = op('base_private_ext')

POP_UP = parent.signals.op('base_modals/popDialog')

def Signalsid(par) -> None:
    pass

def Signalsname(par) -> None:
    pass

def Connected(par) -> None:
    pass

def Controlcomp(par) -> None:
    if par.eval() == None:
        control_comp = SIGNALS.DEFAULT_CUSTOM_PARS
    else:
        control_comp = par.eval()
    
    SIGNALS.ControlComp = control_comp
    SIGNALS.SetControls()

def Customreports(par) -> None:
    pass

#NOTE Advanced Settings
def Manualconfig(par) -> None:

    def _config_callback(info:dict) -> None:
        if info.get('buttonNum') == 2:
            parent.signals.par.Signalsid = info.get('enteredText')
            SIGNALS.Id = info.get('enteredText')
            SIGNALS.Name = "MANUAL_CONFIG"
            op('websocket_signals').par.reset.pulse()

            SIGNALS.SignalsStartUp()
        else:
            pass

    POP_UP.Open(
        title = "Set Signals ID",
        text = "To manually configure signals, please set the Process ID from the Client configuration page",
        buttons = ["Cancel", "Submit"], 
        callback = _config_callback)

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
