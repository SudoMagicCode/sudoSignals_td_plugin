import signalsErrors
import tdDialogHelper

class SignalsIdentity(object):
    '''
    '''
    def __init__(self) -> None:
        self._id = None
        self._name = None
        return
    
    @property
    def Id(self) -> str:
        return self._id

    @Id.setter
    def Id(self, id) -> None:
        if id is None:
            tdDialogHelper.WarnNoProductId()
            raise signalsErrors.IDError("TouchDesigner has no Signals ID")
        self._id = id
        self.SendIdentifyPacket({})
    
    @property
    def Name(self) -> str:
        return self._name

    @Name.setter
    def Name(self, name:str) -> None:
        if name is None:
            tdDialogHelper.WarnNoProductId()
            raise signalsErrors.IDError("TouchDesigner has no Signals ID")
        self._name = name