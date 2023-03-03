import utils
import signalsErrors

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
		controls = []
		pagesToSend = self._controllable.customPages

		for p in pagesToSend:
			newPageDataBlock = {
				"name": p.name,
				"owner": p.owner.path,
				"pars": utils.CreateAllParDataBlocks(p)
			}
			controls.append(newPageDataBlock)
		return controls

	def UpdateControlComp(self, state) -> None:
		if(self._controllable.par[state['name']].style == "Pulse"):
			self._controllable.par[state['name']].pulse()
		else:
			self._controllable.par[state['name']] = state['currentValue']