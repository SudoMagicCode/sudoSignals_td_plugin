




def setPar(data):
	print('')
	thisOp = op(data['op'])
	thisOp.par[data['parName']] = data['value']




SWITCH = {
	"setPar": setPar
}
