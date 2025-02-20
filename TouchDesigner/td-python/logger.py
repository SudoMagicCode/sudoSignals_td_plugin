import utils
import packets

class SignalsLogger:
    def __init__(self):
        self.__logTables = []
        return
    
    def CreateLog(self, logLvl:int, logMsg:str) -> packets.logs.Log:
        newLog = None

        valid_log_lvl = [0, 1, 2, 3, 4]
        log_level_map = [
            packets.log_enums.LOG_LOG,
            packets.log_enums.LOG_INFO,
            packets.log_enums.LOG_WARN,
            packets.log_enums.LOG_CRIT,
            packets.log_enums.LOG_ALERT
        ]
        if logLvl not in valid_log_lvl:
            print(utils.TextPortMsg('WARN', 'Incorrect Log Level || Log level should be a value of 0, 1, 2, 3, 4'))
        else:
            newLog = packets.logs.Log()
            newLog.level = log_level_map[logLvl]
            newLogMessage = packets.log_fields.LogMessage(value=logMsg)
            newLog.message.CopyFrom(newLogMessage)
        return newLog

    def CreateLogFromTable(self, logOp:op) -> packets.logs.Log:
        newLog = None
        valid_log_level = ['0', '1', '2', '3', '4']
        log_level_map = {
            '0':packets.log_enums.LOG_LOG,
            '1':packets.log_enums.LOG_INFO,
            '2':packets.log_enums.LOG_WARN,
            '3':packets.log_enums.LOG_CRIT,
            '4':packets.log_enums.LOG_ALERT
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
                    newLog = packets.logs.Log()
                    newLog.level = log_level_map[logOp[0, 1].val]
                    newLogMessage = packets.log_fields.LogMessage(value=logOp[1, 1].val)
                    newLog.message.CopyFrom(newLogMessage)

        return newLog