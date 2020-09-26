import signals_WSService
import signals_reporter
import signals_controls
import signals_logger
import signals_actions


PARAMS = op('parameter1') 

REPORTINGTIMER = op('timer_reporting')


class Signals:
	def __init__(self, op):
		self._op = op
		self._client = None
		self._productid =  PARAMS['Productid', 'value'].val 
		
		self.startConnection()
		self.startReporting()

	@property
	def Client(self):
		return self._client

	@property
	def ProductId(self):
		return self._productid

	@ProductId.setter
	def ProductId(self, id):
		self._productid = id
		self.startConnection()

	def startConnection(self):
		if self.verify():
			if self._client:
				self._client.Disconnect()
			
			self._client = signals_WSService.Client( self._productid )
			self._client.Connect( onConnect=self.connectedHandler, onReceive=self.dataHandler )

	def endConnection(self):
		self.stopReporting()
		if self._client:
			self._client.Disconnect()
			self._client = None

	def connectedHandler(self):
		self.SendControlsUpdate()
		return

	def dataHandler(self, doc):
		action = doc['action']
		if action in signals_actions.SWITCH:
			signals_actions.SWITCH[action](doc['data'])
		else:
			print(doc)

	def verify(self):
		if self._productid == "":
			signals_logger.Log('Product ID Missing')
			return False

		if self._verifyProductID(self._productid):
			return True
		else: 
			signals_logger.Log('Product ID invalid')
			return False

	def _verifyProductID(self, productID):
		return len(self._productid) > 10

	def startReporting(self):
		REPORTINGTIMER.par.start.pulse()
		return

	def stopReporting(self):
		REPORTINGTIMER.par.init.pulse()
		return

	def SendControlsUpdate(self, userControls={}):
		requiredControls = {"_system": "internalControls"}
		combinedControls = {**requiredControls, **userControls}
		controlForm = signals_controls.GenerateControlsForm(combinedControls)
		controlData = {"controls": controlForm}
		self._client.SendUpdate(controlData)


	def Report(self, userReports={}):
		requiredReports = {"info": "null_DAT_report", "report": "null_CHOP_report"}
		combinedReports = {**requiredReports, **userReports}
		reportData = signals_reporter.GenerateReportData(combinedReports)
		self._client.SendUpdate(reportData)
