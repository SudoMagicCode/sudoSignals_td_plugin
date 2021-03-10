import json
import os

from reporter import SignalsReporter
from controls import SignalsControls
from router import SignalsRouter

WEBSOCKET = op('websocket1')
REPORT_TIMER = op('report_timer')

class SignalsClient(SignalsRouter, SignalsReporter, SignalsControls):
	def __init__(self):
		# Inherit Router
		SignalsRouter.__init__(self, WEBSOCKET)
		# Inherit Reporter
		SignalsReporter.__init__(self)
		# Get current controlComp then inherit Signals
		currentControlComp = op('../').par.Controlcomp.eval()
		SignalsControls.__init__(self, currentControlComp)
		
		# Add Action Routes to hand incoming messages.
		self.AddActionRoute("control-Update", self.UpdateControls)
		
		# Setup Reporting
		self.AddReportable( op('null_defaultReport') )

		# Set Product ID
		self.Id = os.getenv('SIGNALS_ID')

		# Start connection here.
		WEBSOCKET.par.active = 1

		# Send control-Set packet.
		self.SetControls()

		# Start Sending Reports.
		self.SendReport()
		REPORT_TIMER.par.start.pulse()


	def SendReport(self):
		newReportPacket = {
			"action": "report",
			"data": self.CreateReport()
		}
		self.SendMessage(newReportPacket)


	def SetControls(self):
		'''Sends control-Set packet to SudoSginals Desktop Service'''
		controlState = self.CreateControls()
		newControlPacket = {
			"action": "control-Set",
			"data": {"state": controlState}
		}
		self.SendMessage(newControlPacket)


	def UpdateControls(self, packet):
		self.UpdateControlComp(packet['data'])