"""Generates Reports to send to the SudoSignals cloud"""
import signals_logger

def datToJson(dat):
	"""Converts a 2 column TableDAT to a DICT"""
	tempDict = {}
	for row in dat.rows():
		key = row[0].val
		value = row[1].val
		tempDict[key] = value
	return tempDict


def GenerateReportData(template):
	"""Goes through each entry in the template and creates a dict."""
	reportdata = {}
	for key in template:
		theOp = op(template[key]) #DAT to be reported.
		if theOp.isDAT:
			if theOp.numCols > 1:
				reportdata[key] = datToJson( op(template[key]) )
			else:
				signals_logger.Log(f'DAT {theOP.path} is not formatted correctly for the report. DAT must have only 2 Cols [key, val]. omitting.')
		else:
			signals_logger.Log(f'OP {theOP.path} must be a DAT to be included in the report. omitting.')
	return reportdata
