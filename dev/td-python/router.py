import json
import signalsErrors
import tdDialogHelper
import packets
class SignalsRouter(object):
    '''
    '''
    def __init__(self, socket:OP) -> None:
        self._routes = {}
        self._id = None
        self._socket = socket
        self.AddActionRoute(packets.corePackets_pb2.PacketType.START.Name(), self.SendIdentifyPacket)
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

        newPacket = packets.CreateIdentifyPacket(self._id, "TouchDesigner", tdVersion, pluginVersion)
        self.SendMessage(newPacket)

    def RecvMessage(self, message) -> None:
        '''We are receiving a message from the Daemon'''
        newPacket = json.loads(message)
        self._routeMessage(newPacket)

    def RecvBinary(self, contents) -> None:
        '''We are receiving a binary, possible protobuf'''
        packet = packets.corePackets_pb2.CorePacket()
        packet.ParseFromString(contents)
        self._routeBinaryMessage(packet, packet.action)

    def SendMessage(self, packet) -> None:
        if self._id is None:
            print("No id present. Supressing Message.")
            return
        print(packet)
        self._socket.sendText(packet)
        return

    def AddActionRoute(self, routeName, routeFunction) -> None:
        self._routes[routeName] = routeFunction

    def _routeMessage(self, packet) -> None:
        try:
            self._routes[packet["action"]](packet)
        except KeyError:
            print('SIGNALS ROUTER | Action "'+packet['action']+'" is not recognized/implemented.')

    def _routeBinaryMessage(self, packet, route) -> None:
        try:
            self._routes[route](packet)
        except KeyError:
            print('SIGNALS ROUTER | Action "'+packets.corePackets_pb2.PacketType.Name(route)+'" is not recognized/implemented.')
