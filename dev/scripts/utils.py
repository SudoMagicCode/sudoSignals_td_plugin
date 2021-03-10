def parDataBlock(par):
	return {
		"currentValue": par.eval(),
		"name": par.name,
		"label": par.label,
		"path": par.owner.path,
		"type": par.style,
		"index": par.index
	}

def CreateAllParDataBlocks(page):
	parsData = []
	for par in page.pars:
		parsData.append(parDataBlock(par))
	return parsData