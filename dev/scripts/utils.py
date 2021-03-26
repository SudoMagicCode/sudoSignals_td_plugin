def parDataBlock(par, group=False):
	dataBlock = {
		"name": par.name,
		"label": par.label,
		"path": par.owner.path,
		"style": par.style,
		"index": par.index,
		"currentValue": par.eval(),
		"inGroup": group,
	}
	if(par.style == "Menu" or par.style == "StrMenu"):
		dataBlock['menuLabels'] = par.menuLabels
		dataBlock['menuNames'] = par.menuNames
	return dataBlock
	
def groupDataBlock(group):
	if(len(group)>1):
		return {
			"group": True,
			"name": group[0].name,
			"label": group[0].label,
			"style": group[0].style,
			"index": group[0].index,
			"path": group[0].owner.path,
			"pars": [parDataBlock(par, group=True) for par in group]
		}
	else:
		return parDataBlock(group[0], group=False)

def CreateAllParDataBlocks(page):
	parsData = []
	groups = page.parTuplets
	for g in groups:
		parsData.append(groupDataBlock(g))
	return parsData

		
