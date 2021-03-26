import json
import os

from reporter import SignalsReporter
from controls import SignalsControls
from router import SignalsRouter
import tdDialogHelper

WEBSOCKET 			= op('websocket1')
REPORT_TIMER 		= op('report_timer')

LINKS = {
	'Help' 					: "https://sudomagiccode.github.io/SudoSignals/",
	'Forum'					: "https://github.com/SudoMagicCode/SudoSignals/discussions",
	'Sudosignalsdashboard' 	: "https://dashboard.sudosignals.com/",
	'Bugreport'				: "https://forms.clickup.com/f/16ky7-1036/3TNCU1Q2JMMEZ5XS43"
}

class SignalsClient(SignalsRouter, SignalsReporter, SignalsControls):
	
	def __init__(self):
		self.PARSignalsid		= parent.signals.par.Signalsid
		self.PARConnected 		= parent.signals.par.Connected
		self.PARControlcomp 	= parent.signals.par.Controlcomp
		self.PARReports1		= parent.signals.par.Reports1
		self.PARStartupdelay	= parent.signals.par.Startupdelay
		self.signalsReports 	= op('null_defaultReport')

		# Inherit Router
		SignalsRouter.__init__(self, WEBSOCKET)

		# Inherit Reporter
		SignalsReporter.__init__(self)

		# Get current controlComp then inherit Signals
		SignalsControls.__init__(self, self.parControlcomp)

		# Add Action Routes to hand incoming messages.
		self.AddActionRoute("control-Update", self.UpdateControls)
		
		# Setup Reporting
		self.AddReportable( self.signalsReports )

		# Set Product ID
		self._getSignalsId



	###################################
	##### Signals TOX Par Handles #####
	###################################

	@property
	def parSignalsid(self):
		return self.PARSignalsid.eval()

	@parSignalsid.setter
	def parSignalsid(self, parVal):
		parent.signals.par['Signalsid'] = parVal

	@property
	def parConnected(self):
		return self.PARConnected.eval()
	
	@parConnected.setter
	def parConnected(self, parVal):
		parent.signals.par['Connected'] = parVal

	@property
	def parControlcomp(self):
		return self.PARControlcomp.eval()

	@property
	def parReports1(self):
		return self.PARReports1.eval()

	@property
	def parStartupdelay(self):
		return self.PARStartupdelay.eval()

	###################################
	#                                 #
	###################################

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

		signalsId 			= os.getenv('SIGNALS_ID')
		self.parSignalsid 	= signalsId
		self.Id 			= signalsId
		return signalsId

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
		self.parConnected = state

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
		print(f"SUDOSIGNALS :: INFO :: Starting TD Client")
		print('-'*20)

		# Start connection here.
		WEBSOCKET.par.active = 1

		# Send control-Set packet.
		startUpDelayControls = 'args[0].SetControls()'
		run(startUpDelayControls, self, delayFrames=self.parStartupdelay)

		# Start Sending Reports.
		self.SendReport()
		REPORT_TIMER.par.start.pulse()
	
	def PulsePar(self, par):
		'''Signals Start-up Sequence

		Ensures signals start up is consistent, and reliable.
		Waits to send control updates until 60 frames have passed. This
		Should ensure that we've completed any necessary start-up and 
		initialization elements
		
		Args
		----------
		par (TD Parameter)
		> Pulsed parameter object from parent.signals

		Returns 
		----------
		None
		'''

		webLink = LINKS.get(par.name)
		ui.viewFile(webLink)