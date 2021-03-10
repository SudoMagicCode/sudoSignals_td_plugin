import json
import signalsErrors

class SignalsRouter(object):
	def __init__(self, socket):
		self._routes = {}
		self._id = None
		self._socket = socket
		self.AddActionRoute("Start", self.SendIdentifyPacket)
		return

	@property
	def Id(self):
		return self._id

	@Id.setter
	def Id(self, id):
		if id is None:
			raise signalsErrors.IDError
		self._id = id
		self.SendIdentifyPacket({})


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


	def RecvMessage(self, message):
		'''We are receiving a message from the Daemon'''
		newPacket = json.loads(message)
		self._routeMessage(newPacket)

	def SendMessage(self, packet):
		if self._id is None:
			print("No id present. Supressing Message.")
			return
		packet['identifier'] = self._id
		self._socket.sendText(json.dumps(packet))
		return

	def AddActionRoute(self, routeName, routeFunction):
		self._routes[routeName] = routeFunction

	def _routeMessage(self, packet):
		try:
			self._routes[packet["action"]](packet)
		except KeyError:
			print('Action "'+packet['action']+'" is not recognized/implemented.')