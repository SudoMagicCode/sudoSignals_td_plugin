import signals_WSService
import signals_reporter
import signals_controls
import signals_logger
import signals_actions

PARAMS 			= op('parameter1') # Parameters from SudoSignals TOX
REPORTINGTIMER 	= op('timer_reporting') # Timer that triggers regular reporting.
DEVWSS			= "wss://b5eg4qq6bc.execute-api.us-east-1.amazonaws.com/dev"
PRODWSS 			= "wss://603t4a99m8.execute-api.us-east-1.amazonaws.com/prod"

LINKS 			= {
	'Help' 					: "https://api.sudosignals.com/help?version=",
	'Sudosignalsdashboard' 	: "https://dashboard.sudosignals.com/",
	'Bugreport'				: "https://forms.clickup.com/f/16ky7-1036/3TNCU1Q2JMMEZ5XS43"
}

class Signals:    
	"""TouchDesigner Extension that communicates with the SudoSignals Cloud Resources.

    This extension handles the connection, reporting, and setting controls with WS 
	messaging back to the SudoSignals Cloud Resources. 

    Attributes:
        _op: A TouchDesigner Operator that runs this extension.
        _client: A WS Client that formats and sends messages.
		_productid: A string is used to identify this installation.
    """
	def __init__(self, myOp):
		"""Inits Signals and attempts to start a connection and reporting."""
		self._op = myOp
		self._client = None
		
		# point to target par for prodcut id, None as default, attempt to eval the par
		self._productidPar	 	= op('../').par.Productid
		self._productid 		= None
		self.UpdateProductId()

		# point to target par for control comp, None as default, attempt to eval the par
		self._controlCompPar 	= op('../').par.Controlcomp
		self._controlComp		= None
		self.UpdateControlComp()

		self.startConnection()
		self.startReporting()
		# TODO (IS): We should probably send the current state of the controls on init.

	@property
	def Client(self):
		"""Exposes the client as a property"""
		return self._client

	# - - - - - - - - Prodcut ID - - - - - - - - 
	@property
	def ProductId(self):
		"""Exposes the productid as a property"""
		return self._productid

	@ProductId.setter
	def ProductId(self, id):
		"""When the productid is set we should restart the connection"""
		self._productid = id
		self.endConnection()
		self.startConnection()

	@property
	def hasProductId(self):
		return True if self._productid is not '' else False

	def UpdateProductId(self):
		self._productid = self._productidPar.eval()
		self.endConnection()
		self.startConnection()
		pass

	# - - - - - - - - Control COMP - - - - - - - - 
	@property
	def ControlComp(self):
		return self._controlComp
	
	@ControlComp.setter
	def ControlComp(self, targetComp):
		self._controlComp = targetComp
		self.startConnection()

	@ControlComp.setter
	def ControlComp(self, targetComp):
		self._controlComp = targetComp

	def UpdateControlComp(self):
		self._controlComp = self._controlCompPar.eval()
		self.startConnection()

	# - - - - - - - - Singnals Operations - - - - - - - - 
	def startConnection(self, dev=False):
		"""Verifies the ProductId property is structured correctly and starts a connection."""
		# ProductId is formatted correctly

		print("starting connection")
		WssAddress = PRODWSS

		if dev:
			WssAddress = DEVWSS
		else:
			pass

		if self._client:
			# A client already exists... might be connected...
			self._client.Disconnect()
		if self.verify():
			# Create a new Client.
			self._client = signals_WSService.Client( self._productid )
			print("creating a new client")
			# Start Connection. Populate the onConnect and onReceive Callbacks.
			print("starting a new connection")
			self._client.Connect( onConnect=self.connectedHandler, 
									onReceive=self.dataHandler,
									address= WssAddress)
			op('../').par.Connected = True

	def SetDev(self):
		self._endConnection()
		self.startConnection(dev=True)
		pass

	def SetProd(self):
		self._endConnection()
		self.startConnection(dev=False)
		pass

	def endConnection(self):
		self._endConnection()

	def _endConnection(self):
		"""End Signals connection and reporting."""
		self.stopReporting()
		if self._client:
			# A client Exists... disconnect it.
			self._client.Disconnect()
			self._client = None
			op('../').par.Connected = False

	def connectedHandler(self):
		"""This is used as a callback once the client Connects."""

		print("now connected")

		# Send the controls to the sudosignals service.
		self.startReporting()
		self.SendControlsUpdate()
		return

	def dataHandler(self, doc):
		"""A Callback for handling receiving data from the WS connection."""
		
		# Get the Action Type
		action = doc['action']
		
		# Look up the Action in the signals_actions API
		if action in signals_actions.SWITCH:
			# This action is defined in the API.
			# Run the function and pass in the data received.  
			signals_actions.SWITCH[action](doc['data'])
		else:
			# This action is not defined in the API
			# Print it.
			print(doc)

	def verify(self):
		"""Verifies the productid is valid."""
		if self._productid == "" or self._productid == None:
			# ProductID is empty.
			signals_logger.Log('Product ID Missing')
			return False

		if self._verifyProductID(self._productid):
			# productid is Valid.
			return True
		else: 
			# productid is not Valid.
			signals_logger.Log('Product ID invalid')
			return False

	def _verifyProductID(self, productID):
		"""Validates the ProductID"""
		# this is a simple validation process
		# TODO (IS): There is probably more we can do here to validate.
		return len(self._productid) > 10

	def startReporting(self):
		"""Starts the reporting process."""
		REPORTINGTIMER.par.start.pulse()
		return

	def stopReporting(self):
		"""Stops the reporting process."""
		REPORTINGTIMER.par.initialize.pulse()
		return

	def SendControlsUpdate(self, userControls={}):
		"""Compiles the control update packet and sends it.
		
		:param userControls: a dict where keys are control labels and values are op paths
		"""

		# dict of required comps
		requiredControls = {"_system": "internalControls",
							"_userDefined": self.ControlComp} 
		# combine required and user submitted.
		combinedControls = {**requiredControls, **userControls}

		# generate the structured message 
		controlForm = signals_controls.GenerateControlsForm(combinedControls)

		# create its highlevel key.
		controlData = {"controls": controlForm}
		
		# only send if we have a valid product ID
		if self.hasProductId:
			# Send it. 
			self._client.SendUpdate(controlData)

	def Report(self, userReports={}):
		"""Compiles all of the reports and sends it.
		
		:param userReports: a dict where keys are report labels and values are DATs to be reported
		"""		

		# dict of required reports
		requiredReports = {"info": "null_DAT_report", "report": "null_CHOP_report"}
		# combine required with user reports
		combinedReports = {**requiredReports, **userReports}
		
		# Generate the structured reports.
		reportData = signals_reporter.GenerateReportData(combinedReports)
		
		# check for a product ID
		if self.hasProductId:
			# Send it.
			self._client.SendUpdate(reportData)
		
		else:
			pass

	def Alert(self, aType, data):
		"""Triggers an alert"""
		if op('parameter1')['Usealerts', 1] == 1:
			data["alertType"] =  aType
			if not ui.performMode and op('parameter1')['Silence', 1] == 0:
				# We are in Network Editor mode and not silenced.
				self._client.SendAlert(data)
			elif ui.performMode:
				# We are in Perform mode.
				self._client.SendAlert(data)
			else:
				pass

	

	def PulsePar(self, parName):
		""" Dictionary Lookup for links
		"""
		link 	= LINKS.get(parName)

		if parName == 'Help':
			ui.viewFile(f'{link}{self._op.par.Version.eval()}')
		else:
			ui.viewFile(link)
