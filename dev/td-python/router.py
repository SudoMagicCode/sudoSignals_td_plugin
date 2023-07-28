import json
import signalsErrors
import tdDialogHelper

class SignalsRouter(object):
    '''
    '''
    def __init__(self, socket:OP) -> None:
        self._routes = {}
        self._id = None
        self._socket = socket
        self.AddActionRoute("Start", self.SendIdentifyPacket)
        return

    @property
    def Id(self) -> str:
        return self._id

    @Id.setter
    def Id(self, id) -> None:
        if id is None:
            # tdDialogHelper.WarnNoProductId()
            raise signalsErrors.IDError("TouchDesigner has no Signals ID")
        self._id = id
        self.SendIdentifyPacket({})

    def SendIdentifyPacket(self, data) -> None:
        '''Sends identity packet to SudoSignals Desktop Service'''
        tdVersion = f"{app.version} {app.build}"
        pluginVersion = parent.signals.par.Version.eval()
        newIdentifyPacket = {
            "action": "identify", 
            "data": {
                "SoftwareName": "TouchDesigner", 
                "SoftwareVersion": tdVersion,
                "PluginVersion" : pluginVersion
            }
        }
        self.SendMessage(newIdentifyPacket)

    def RecvMessage(self, message) -> None:
        '''We are receiving a message from the Daemon'''
        newPacket = json.loads(message)
        self._routeMessage(newPacket)

    def SendMessage(self, packet) -> None:
        if self._id is None:
            print("No id present. Supressing Message.")
            return
        packet['identifier'] = self._id
        # debug(packet)
        self._socket.sendText(json.dumps(packet))
        return

    def AddActionRoute(self, routeName, routeFunction) -> None:
        self._routes[routeName] = routeFunction

    def _routeMessage(self, packet) -> None:
        try:
            self._routes[packet["action"]](packet)
        except KeyError:
            print('SIGNALS ROUTER | Action "'+packet['action']+'" is not recognized/implemented.')