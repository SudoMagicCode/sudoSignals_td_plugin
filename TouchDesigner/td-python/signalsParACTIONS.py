from __future__ import annotations

try: 
    import signalsTDPluginEXT
except:
    pass

# type hinting used for code completion
SIGNALS:signalsTDPluginEXT.SignalsClient = op('base_private_ext')
SIGNALS_COMP = parent.signals

POP_UP = op('base_modals/popDialog')

def Signalsid(par) -> None:
    """Run when changes occur on the Signalsid parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    pass

def Signalsname(par) -> None:
    """Run when changes occur on the Signalsname parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    pass

def Connected(par) -> None:
    """Run when changes occur on the Connected parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    pass

def Controlcomp(par) -> None:
    """Run when changes occur on the Controlcomp parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    if par.eval() == None:
        control_comp = SIGNALS.DEFAULT_CUSTOM_PARS
    else:
        control_comp = par.eval()
    
    SIGNALS.ControlComp = control_comp
    SIGNALS.SetControls()

def Customreports(par) -> None:
    """Run when changes occur on the Customreports parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    pass

#NOTE Advanced Settings
def Manualconfig(par) -> None:
    """Run when changes occur on the Manualconfig parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    print(par.eval())
    if par.eval():
        # when going form off to on, we change the read only state,
        # and request the Process ID from the user.
        read_only_state = False
    
    else:
        # Turn on readonly state
        # empty Signalsid parameter
        # toggle off connected state
        # the Signals tox should not be reset for connecting with Signals
        # automatically
        read_only_state = True
        SIGNALS.Id = ''
        SIGNALS_COMP.par.Signalsid = ''
        SIGNALS_COMP.par.Connected = False
    
    print(read_only_state, par.eval())
    SIGNALS_COMP.par.Signalsid.readOnly = read_only_state
    SIGNALS_COMP.par.Resetconnection.pulse()

def Startupdelay(par) -> None:
    """Run when changes occur on the Startupdelay parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    pass

def Resetconnection(par) -> None:
    """Run when changes occur on the Resetconnection parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    SIGNALS.par.reinitextensions.pulse()
    SIGNALS.SignalsStartUp()

#NOTE About Page
def Help(par) -> None:
    """Run when changes occur on the Help parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    webLink = SIGNALS.LINKS.get('Help')
    ui.viewFile(webLink)

def Sudosignalsdashboard(par) -> None:
    """Run when changes occur on the Sudosignalsdashboard parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    webLink = SIGNALS.LINKS.get('Sudosignalsdashboard')
    ui.viewFile(webLink)

def Forum(par) -> None:
    """Run when changes occur on the Forum parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    webLink = SIGNALS.LINKS.get('Forum')
    ui.viewFile(webLink)

def Bugreport(par) -> None:
    """Run when changes occur on the Bugreport parameter
    
    Args
    ----------
    par (`TD_par`)
    > Changed parameter from TouchDesigner, this is a par object.

    Returns 
    ----------
    None
    """
    webLink = SIGNALS.LINKS.get('Bugreport')
    ui.viewFile(webLink)
