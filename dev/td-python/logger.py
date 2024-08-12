import utils
import packets

class SignalsLogger:
    def __init__(self):
        self.__logTables = []
        return
    
    def CreateLog(self, logLvl:int, logMsg:str) -> packets.fieldTypes_pb2.Log:
        newLog = None

        valid_log_lvl = [0, 1, 2, 3, 4]
        log_level_map = [
            packets.signalsEnums_pb2.LogLevel.LOG,
            packets.signalsEnums_pb2.LogLevel.INFO,
            packets.signalsEnums_pb2.LogLevel.WARN,
            packets.signalsEnums_pb2.LogLevel.CRIT,
            packets.signalsEnums_pb2.LogLevel.ALERT
        ]
        if logLvl not in valid_log_lvl:
            print(utils.TextPortMsg('WARN', 'Incorrect Log Level || Log level should be a value of 0, 1, 2, 3, 4'))
        else:
            newLog = packets.fieldTypes_pb2.Log()
            newLog.level = log_level_map[logLvl]
            newLog.message = logMsg
        return newLog

    def CreateLogFromTable(self, logOp:op) -> packets.fieldTypes_pb2.Log:
        newLog = None
        valid_log_level = ['0', '1', '2', '3', '4']
        log_level_map = {
            '0':packets.signalsEnums_pb2.LogLevel.LOG,
            '1':packets.signalsEnums_pb2.LogLevel.INFO,
            '2':packets.signalsEnums_pb2.LogLevel.WARN,
            '3':packets.signalsEnums_pb2.LogLevel.CRIT,
            '4':packets.signalsEnums_pb2.LogLevel.ALERT
        }
        
        #check to ensure op is table
        if logOp.type != 'table':
            print(utils.TextPortMsg('WARN', 'Incorrect Log Op Type || Operator type should be TableDAT'))
        else:
            # check to ensure table DAT is the correct size
            if logOp.numCols != 2 and logOp.numRows != 2:
                print(utils.TextPortMsg('WARN', 'Incorrect Table Size || Table DAT should be 2 x 2'))
            else:
                # check to ensure log level is valid entry
                if logOp[0, 1].val not in valid_log_level:
                    print(utils.TextPortMsg('WARN', 'Incorrect Log Level || Log level should be a value of 0, 1, or 2'))
                else:
                    newLog = packets.fieldTypes_pb2.Log()
                    newLog.level = log_level_map[logOp[0, 1].val]
                    newLog.message = logOp[1, 1].val

        return newLog