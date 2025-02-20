import google.protobuf
import google.protobuf.struct_pb2
import packets
import google
import time
class SignalsReporter:
	def __init__(self):
		self._pendingReportables = []
		self._reportables = []
		self.dataFields = {}
		return
	
	def _pollFields(self):
		for r in self._reportables:
			for row in r.rows():
				key = row[0].val
				value = row[1].val
				fieldHash = r.name+":"+key
				dataField = None
				if fieldHash in self.dataFields:
					dataField = self.dataFields[fieldHash]
				else:
					newDataField = packets.report_fields.DataField()
					newDataField.name = key
					newDataField.type = packets.report_enums.NUMBER
					self.dataFields[fieldHash] = newDataField
					dataField = newDataField
				newVal = google.protobuf.struct_pb2.Value()
				newVal.number_value = float(value)
				dataField.values.append(newVal)
		return 
	
	def CreateDataFrame(self) -> packets.report_fields.DataFrame:
		self._pollFields()
		newDataFrame = packets.report_fields.DataFrame()
		newDataFrame.fields.extend(list(self.dataFields.values()))
		self.dataFields = {}
		self._reportables.extend(self._pendingReportables)
		self._pendingReportables = []
		return newDataFrame


	def AddReportable(self, op) -> callable:
		if op.isDAT:
			if op.numCols > 2:
				print("SIGNALS WARNING: Reportable OP '"+op.path+"' has more than 2 columns.\nSignals will use only the first 2 columns to build reports.")
			elif op.numCols < 2:
				print("SIGNALS WARNING: Reportable OP '"+op.path+"' has less than 2 columns.\nSignals needs at least 2 columns to add this as a reportable.")
				return
		else:
			print("SIGNALS WARNING: Reportable OP '"+op.path+"' is not a DAT.\nSignals will use only DAT operators to create reports.")
			return
		self._pendingReportables.append(op)