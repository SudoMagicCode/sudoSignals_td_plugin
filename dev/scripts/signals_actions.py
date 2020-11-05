""" Actions for SudoSignals are defined here.

Actions are functions that happen when SudoSignals receives a message 
from the WS connection. Each message contains an "action" key which 
is used to call the appropriate function.

A new action must except one argument which is a dict containing the
message information. The action must then be added to the SWITCH dict
with the action key which will trigger the call. 

TODO (IS): Actions to be created - setScene, forceReport, runScript
"""




def setPar(data):
	# print(data)
	thisOp = op(data['op'])
	if thisOp.par[data['parName']].isPulse:
		if data['value'] == 1:
			thisOp.par[data['parName']].pulse()
	else:
		thisOp.par[data['parName']] = data['value']


SWITCH = {
	"setPar": setPar
}
