CHOPREPORT = op('null_CHOP_report')
DATREPORT = op('null_DAT_report')


def datToJson(dat):
	tempDict = {}
	for row in dat.rows():
		key = row[0].val
		value = row[1].val
		tempDict[key] = value
	return tempDict


class Reporter:
	def __init__(self):
		return

	def GenerateReport(self):
		report = {}
		report["chop"] = datToJson(CHOPREPORT)
		report["dat"] = datToJson(DATREPORT)
		return report

	def SendReport(self):
		parent().Send(self.GenerateReport())
		return