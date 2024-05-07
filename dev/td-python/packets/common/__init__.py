try:
	import dynamo_pb2
	import fieldTypes_pb2
	import packets_pb2
	import payloads_pb2
	import signalsEnums_pb2
	import signalsOptions_pb2
except:
	print("[~] WARNING! Could not import protobuf types. Please add them to the python path.")