import json

import reporter 
from router import SignalsRouter
import utils

WEBSOCKET = op('websocket1')
REPORT_TIMER = op('report_timer')

INSTANCE_ID = "TOUCHDESIGNER_OMG"

class SignalsClient(SignalsRouter):
	def __init__(self):
		super().__init__(WEBSOCKET)
		# Add Action Routes to hand incoming messages.
		self.AddActionRoute("Start", self.SendIdentifyPacket)
		self.AddActionRoute("control-Update", self.UpdateControls)
		
		# Setup Reporting
		self._reporter = reporter.Reporter()
		self._reporter.AddReportable(op('null_defaultReport'))

		# Set Product ID
		self.ProductId = INSTANCE_ID

		# Start connection here.
		WEBSOCKET.par.active = 1

		# Send control-Set packet.
		self._controlsComp = op('base1')
		self.SetControls()

		# Start Sending Reports.
		REPORT_TIMER.par.start.pulse()

	@property
	def ControlComp(self):
		return self._controlsComp

	@ControlComp.setter 
	def ControlComp(self, op):
		self._controlsComp = op
		self.SetControls()

	def SendIdentifyPacket(self, data):
		'''Sends identity packet to SudoSignals Desktop Service'''
		newIdentifyPacket = {
			"action": "identify", 
			"data": {
				"SoftwareName": "TouchDesigner", 
				"SoftwareVersion": "TouchDesignerVersion"
			}
		}
		self.SendMessage(newIdentifyPacket)


	def SendReport(self):
		newReportPacket = {
			"action": "report",
			"data": self._reporter.CreateReport()
		}
		self.SendMessage(newReportPacket)


	def SetControls(self):
		'''Sends control-Set packet to SudoSginals Desktop Service'''
		controls = []
		pagesToSend = self._controlsComp.customPages
		
		for p in pagesToSend:
			newPageDataBlock = {
				"name": p.name,
				"owner": p.owner.path,
				"pars": utils.CreateAllParDataBlocks(p)
			}
			controls.append(newPageDataBlock)
		
		newSetControlsPacket = {
			"action": "control-Set", 
			"data": controls
		}
		self.SendMessage(newSetControlsPacket)


	def UpdateControls(self, data):
		print("____control-Update____")
		print(data)