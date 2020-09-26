import json

WEBSOCKET = op('websocket1')
RETRYTIMER = op('timer_connection')

class Client:
	"""A Websocket client that connects back to SudoSignal Cloud"""
	def __init__(self, installationid):
		self.installationID = installationid
		self.connected = False
		self.address = ""
		self._receivedCB = None
		self._connectedCB = None
		return

	def _connect(self):
		WEBSOCKET.par.netaddress = self.address
		WEBSOCKET.par.active = 1
		return

	def _disconnect(self):
		WEBSOCKET.par.active = 0
		self.connected = False
		return

	def _send(self, doc):
		doc['installationid'] = self.installationID
		WEBSOCKET.sendText(json.dumps(doc))
		return

	def _receive(self, sDoc):
		doc = json.loads(sDoc)
		tryCB(self._receivedCB, arg=doc)
		return

	def _onConnect(self):
		if self.installationID:

			self.connected = True
			
			#send Own Packet
			self._send({"action": "own", "installationid": self.installationID})
			tryCB(self._connectedCB)
		else:
			#we can't own the installation yet... disconnect to save resources.
			self._disconnect()
			raise Exception("installation ID is not set.")

		return

	def _onDisconnect(self):
		self._disconnect()
		if self.installationID:
			RETRYTIMER.par.start.pulse()
		else:
			return

	def Send(self, doc):
		self._send(doc)
		return

	def Receive(self, sDoc):
		self._receive(sDoc)
		return

	def Connected(self):
		self._onConnect()
		return

	def Disconnected(self):
		self._onDisconnect()
		return

	def SendUpdate(self, data):
		data["action"] = "update"
		self.Send(data)
		return
		
	def Disconnect(self):
		self._disconnect()
		return
		
	def Connect(self, onConnect=None, onReceive=None, address="wss://qsnzjcchgg.execute-api.us-east-1.amazonaws.com/dev"):
		self._receivedCB = onReceive
		self._connectedCB = onConnect
		self.address = address
		self._connect()
		return
		
	def SetInstallationID(self, id):
		self.installationID = id
		return



def tryCB(cb, arg=None):
	if cb is None:
		return
	if callable(cb):
		try:
			if(arg):
				cb(arg)
			else:
				cb()
		except Exception as e:
			print(e)
	else:
		print("cb is not callable.")
