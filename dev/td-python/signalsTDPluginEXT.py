import json
import os

from reporter import SignalsReporter
from controls import SignalsControls
from router import SignalsRouter
from logger import SignalsLogger

import tdDialogHelper
import utils
import packets

WEBSOCKET = op('websocket_signals')
REPORT_TIMER = op('report_timer')
RELEASE_SOURCE = "https://github.com/SudoMagicCode/sudoSignals_td_plugin_releases/releases/latest"

class SignalsClient(SignalsRouter, SignalsReporter, SignalsControls, SignalsLogger):
    """SiganlsClient Doc Strings
    """
    
    LINKS = {
        'Help' 					: "https://sudomagiccode.github.io/SudoSignals/",
        'Forum'					: "https://github.com/SudoMagicCode/SudoSignals/discussions",
        'Sudosignalsdashboard' 	: "https://dashboard.sudosignals.com/",
        'Bugreport'				: "https://forms.clickup.com/f/16ky7-1036/3TNCU1Q2JMMEZ5XS43"
    }
    DEFAULT_CUSTOM_PARS = op('base_default_custom_pars')

    def __init__(self):
        self.PARSignalsid		= parent.signals.par.Signalsid
        self.PARSignalsName 	= parent.signals.par.Signalsname
        self.PARConnected 		= parent.signals.par.Connected
        self.PARControlcomp 	= parent.signals.par.Controlcomp
        self.PARStartupdelay	= parent.signals.par.Startupdelay
        self.PARManualconfig    = parent.signals.par.Manualconfig
        self.signalsReports 	= op('null_defaultReport')

        self._reset_websocket(WEBSOCKET)

        # Inherit Router
        SignalsRouter.__init__(self, WEBSOCKET)

        # Inherit Reporter
        SignalsReporter.__init__(self)

        # Get current controlComp then inherit Signals
        SignalsControls.__init__(self, self.PARControlcomp.eval())

        #Inherit Signals Logger
        SignalsLogger.__init__(self)

        # Set Product ID
        self._getSignalsId

        # Set Product Name
        self._getSignalsName

        # Add Action Routes to hand incoming messages.
        self.AddActionRoute("control-Update", self.UpdateControls)
        
        # Setup Reporting
        self.AddReportable( self.signalsReports )

        print(utils.TextPortMsg('INFO', 'Signals EXT Init'))
        # self.SetLog(0, '[*] :: SudoSignals TouchDesigner Plugin Initialized')

    @property
    def parSignalsName(self):
        return self.PARSignalsName.eval()

    @property
    def parSignalsid(self):
        return self.PARSignalsid.eval()

    @property
    def parConnected(self):
        return self.PARConnected.eval()
    
    @property
    def parControlcomp(self):
        return self.PARControlcomp.eval()

    @property
    def parReports1(self):
        return self.PARReports1.eval()

    @property
    def parStartupdelay(self):
        return self.PARStartupdelay.eval()

    @property
    def _getSignalsId(self):
        """Updates Signals ID - both member and par
        
        Args
        ----------
        None

        Returns 
        ----------
        signalsId (str)
        > signals ID string retrieved from the signals env var
        """

        if self.PARManualconfig.eval():
            signalsId = self.PARSignalsid.eval()

        else:
            try:
                signalsId = me.var('SIGNALS_ID')
            except:
                signalsId = 'no_id_assigned'

        self.PARSignalsid.val = signalsId
        self.Id = signalsId
        return signalsId

    @property
    def _getSignalsName(self):
        """Updates Signals Name - both member and par
        
        Args
        ----------
        None

        Returns 
        ----------
        signalsName (str)
        > signals Name string retrieved from the signals env var
        """		

        try:
            signalsName = me.var('SIGNALS_NAME')
        except:
            signalsName = 'no_name_assigned'

        self.PARSignalsName.val	= signalsName
        self.Name = signalsName
        return signalsName

    @property
    def hasValidSignalsId(self):
        return True if self.Id is not None else False

    def SendReport(self):
        newDataFrame = self.CreateDataFrame()
        newDataFrame.name = self.parSignalsid

        newReportPacket = packets.CreateReportPacket(newDataFrame)

        self.SendMessage(newReportPacket)

    def SendLog(self, log:packets.fieldTypes_pb2.Log) -> None:
        if log == None:
            print(utils.TextPortMsg('WARN', 'Log suppressed - Nonetype received'))

        else:
            newLogPacket = packets.CreateLogPacket(log.level,log.message)
            self.SendMessage(newLogPacket)        

    def SetLog(self, logLvl:int, logMsg:str) -> None:
        newLog = self.CreateLog(logLvl, logMsg)
        self.SendLog(newLog)

    def SetControls(self):
        """Sends control-Set packet to SudoSignals Desktop Service
        """

        #controlState = self.CreateControls()
        #newControlPacket = {
        #    "action": "control-Set",
        #    "data": {"state": controlState}
        #}

        controlPages = self.CreateControls()
        newControlPacket = packets.CreateControlPacket(controlPages)
        self.SendMessage(newControlPacket)

    def SetLogFromTable(self, LogOp:op) -> None:
        """Sends log info to SudoSignals Desktop Service
        """

        newLog = self.CreateLogFromTable(LogOp)
        self.SendLog(newLog)
        
        # clear message
        LogOp[1, 1] = ''

    def UpdateControls(self, packet):
        self.UpdateControlComp(packet['data'])

    def UpdateConnected(self, state):
        self.PARConnected.val = state

    def SignalsStartUp(self):
        """Signals Start-up Sequence

        Ensures signals start up is consistent, and reliable.
        Waits to send control updates until 60 frames have passed. This
        Should ensure that we've completed any necessary start-up and 
        initialization elements
        
        Args
        ----------
        None

        Returns 
        ----------
        None
        """
        print('-'*20)
        print(utils.TextPortMsg('INFO', 'Starting TD Client'))
        print('-'*20)

        self._reset_websocket(WEBSOCKET)

        # Start connection here.
        WEBSOCKET.par.active = 1

        # Send control-Set packet.
        startUpDelayControls = 'args[0].SetControls()'
        run(startUpDelayControls, self, delayFrames=self.parStartupdelay)

        # Start Sending Reports.
        self.SendReport()
        REPORT_TIMER.par.start.pulse()

    def Clean_up(self) -> None:
        self._clean_up()

    def _clean_up(self) -> None:
        parent.signals.par.Connected = False

    def _reset_websocket(self, websocket:callable) -> None:
        websocket.par.reset.pulse()