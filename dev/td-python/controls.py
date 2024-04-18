import utils
import signalsErrors
import packets

class SignalsControls:
	def __init__(self, op:OP) -> None:
		self._controllable = op
		return
		
	@property
	def ControlComp(self) -> callable:
		return self._controllable

	@ControlComp.setter
	def ControlComp(self, op):
		self._controllable = op

	def CreateControls(self) -> list:
		controlPages = []
		pagesToSend = self._controllable.customPages

		for idx, p in enumerate(pagesToSend):
			newControlPage = packets.fieldTypes_pb2.ControlPage()
			newControlPage.name = p.name
			newControlPage.uuid = p.owner.path+"#"+str(idx)

			newControls = utils.CreateAllParDataBlocks(p)
			for k,v in newControls.items():
				newControlPage.controls[k].CopyFrom(v)
			controlPages.append(newControlPage)
		return controlPages

	def UpdateControlComp(self, state) -> None:
		if(self._controllable.par[state['name']].style == "Pulse"):
			self._controllable.par[state['name']].pulse()
		else:
			self._controllable.par[state['name']] = state['currentValue']