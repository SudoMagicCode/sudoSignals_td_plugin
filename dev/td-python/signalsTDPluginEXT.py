import json
import os

from reporter import SignalsReporter
from controls import SignalsControls
from router import SignalsRouter
import tdDialogHelper
import utils

WEBSOCKET = op('websocket_signals')
REPORT_TIMER = op('report_timer')
RELEASE_SOURCE = "https://github.com/SudoMagicCode/sudoSignals_td_plugin_releases/releases/latest"

class SignalsClient(SignalsRouter, SignalsReporter, SignalsControls):
    '''SiganlsClient Doc Strings
    '''
    
    LINKS = {
        'Help' 					: "https://sudomagiccode.github.io/SudoSignals/",
        'Forum'					: "https://github.com/SudoMagicCode/SudoSignals/discussions",
        'Sudosignalsdashboard' 	: "https://dashboard.sudosignals.com/",
        'Bugreport'				: "https://forms.clickup.com/f/16ky7-1036/3TNCU1Q2JMMEZ5XS43"
    }
    
    def __init__(self):
        self.PARSignalsid		= parent.signals.par.Signalsid
        self.PARSignalsName 	= parent.signals.par.Signalsname
        self.PARConnected 		= parent.signals.par.Connected
        self.PARControlcomp 	= parent.signals.par.Controlcomp
        self.PARStartupdelay	= parent.signals.par.Startupdelay
        self.signalsReports 	= op('null_defaultReport')

        # Inherit Router
        SignalsRouter.__init__(self, WEBSOCKET)

        # Inherit Reporter
        SignalsReporter.__init__(self)

        # Get current controlComp then inherit Signals
        SignalsControls.__init__(self, self.PARControlcomp.eval())

        # Add Action Routes to hand incoming messages.
        self.AddActionRoute("control-Update", self.UpdateControls)
        
        # Setup Reporting
        self.AddReportable( self.signalsReports )

        # Set Product ID
        self._getSignalsId

        # Set Product Name
        self._getSignalsName

        print(utils.TextPortMsg('INFO', 'Signals EXT Init'))

    ###################################
    ##### Signals TOX Par Handles #####
    ###################################

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
        '''Updates Signals ID - both member and par
        
        Args
        ----------
        None

        Returns 
        ----------
        signalsId (str)
        > signals ID string retrieved from the signals env var
        '''

        try:
            signalsId = os.getenv('SIGNALS_ID')
        except:
            signalsId = 'no_id_assigned'


        self.PARSignalsid.val = signalsId
        self.Id = signalsId
        return signalsId

    @property
    def _getSignalsName(self):
        '''Updates Signals Name - both member and par
        
        Args
        ----------
        None

        Returns 
        ----------
        signalsName (str)
        > signals Name string retrieved from the signals env var
        '''		

        signalsName = os.getenv('SIGNALS_NAME')
        self.PARSignalsName.val	= signalsName
        return signalsName


    @property
    def hasValidSignalsId(self):
        return True if self.Id is not None else False

    def SendReport(self):
        '''Sends Reports
        
        Args
        ----------
        None

        Returns 
        ----------
        None
        '''
        newReportPacket = {
            "action": "report",
            "data": self.CreateReport()
        }
        self.SendMessage(newReportPacket)

    def SendLog(self):
        '''Sends Reports
        
        Args
        ----------
        None

        Returns 
        ----------
        None
        '''
        newLogPacket = {
            "action": "log",
            "data": self.CreateLog()
        }
        self.SendMessage(newLogPacket)

    def SetControls(self):
        '''Sends control-Set packet to SudoSginals Desktop Service
        
        Args
        ----------
        None

        Returns 
        ----------
        None
        '''

        controlState = self.CreateControls()
        newControlPacket = {
            "action": "control-Set",
            "data": {"state": controlState}
        }
        self.SendMessage(newControlPacket)

    def UpdateControls(self, packet):
        self.UpdateControlComp(packet['data'])

    def UpdateConnected(self, state):
        self.PARConnected.val = state

    def SignalsStartUp(self):
        '''Signals Start-up Sequence

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
        '''
        print('-'*20)
        print(utils.TextPortMsg('INFO', 'Starting TD Client'))
        print('-'*20)

        # Start connection here.
        WEBSOCKET.par.active = 1

        # Send control-Set packet.
        startUpDelayControls = 'args[0].SetControls()'
        run(startUpDelayControls, self, delayFrames=self.parStartupdelay)

        # Start Sending Reports.
        self.SendReport()
        REPORT_TIMER.par.start.pulse()
