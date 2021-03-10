class Reporter:
	def __init__(self):
		self._reportables = []
		return
	
	def CreateReport(self):
		newReport = []
		for r in self._reportables:
			for row in r.rows():
				key = row[0].val
				value = row[1].val
				newReport.append({"label": key, "value": value})
		return {"kpis": newReport}

	def AddReportable(self, op):
		if op.isDAT:
			if op.numCols > 2:
				print("SIGNALS WARNING: Reportable OP '"+op.path+"' has more than 2 columns.\nSignals will use only the first 2 columns to build reports.")
			elif op.numCols < 2:
				print("SIGNALS WARNING: Reportable OP '"+op.path+"' has less than 2 columns.\nSignals needs at least 2 columns to add this as a reportable.")
				return
		else:
			print("SIGNALS WARNING: Reportable OP '"+op.path+"' is not a DAT.\nSignals will use only DAT operators to create reports.")
			return
		self._reportables.append(op)