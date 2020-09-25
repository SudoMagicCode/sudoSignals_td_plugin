""" A TouchDesigner Module that structures Custom Parameters in COMP to be sent to SudoSignals."""

import json
import time 

def packTuplet(tuplet):
	"""Packs a tuplet with correct label and order"""
	packedTuplet = {}
	packedTuplet['label'] = tuplet[0].label
	packedTuplet['pars'] = [packPar(thisPar) for thisPar in tuplet] 
	packedTuplet['order'] = tuplet[0].order
	return packedTuplet

def packPar(par):
	"""Packs a par with information to reconstruct in SudoSignals"""
	packedPar = {}
	packedPar['name'] = par.name
	packedPar['op'] = par.owner.path
	packedPar['value'] = par.eval()
	packedPar['type'] = par.style
	packedPar['vecIndex'] = par.vecIndex
	if(par.style == "Menu" or par.style == "StrMenu"):
		packedPar['menuLabels'] = par.menuLabels
		packedPar['menuNames'] = par.menuNames
	return packedPar 

def makeForm(op):
	"""Pack all of the pages into separate keys."""
	form = []
	pages = op.customPages
	for page in pages:
		
		allTuplets = page.parTuplets
		allPackedTuplets = [packTuplet(thisTuplet) for thisTuplet in allTuplets]
		pageTemplate = {"name": page.name, "tuplets": allPackedTuplets}
		form.append(pageTemplate)
	return form

def GenerateControlsForm(template):
	"""Create a key per operator and generate a form for all pages and params"""
	ControlsForm = {}
	for key in template:
		theOp = op(template[key])
		theOpForm = makeForm(theOp)
		ControlsForm[key] = {"_op": theOp.path, "form": theOpForm}
	ControlsForm['timestamp'] = time.time()
	return ControlsForm 
