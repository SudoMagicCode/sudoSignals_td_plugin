import utils

class SignalsLogger:
    def __init__(self):
        self.__logTables = []
        return
    
    def CreateLog(self, logLvl:int, logMsg:str) -> dict:
        newLog = None

        valid_log_lvl = [0, 1, 2]
        if logLvl not in valid_log_lvl:
            print(utils.TextPortMsg('WARN', 'Incorrect Log Level || Log level should be a value of 0, 1, or 2'))
        else:
            newLog = {
                'logLevel' : logLvl,
                'message' : logMsg
            }
        return newLog

    def CreateLogFromTable(self, logOp:op) -> dict:
        newLog = None
        valid_log_level = ['0', '1', '2']
        
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
                    newLog = {
                        'logLevel' : int(logOp[0, 1].val),
                        'message' : logOp[1, 1].val			
                    }

        return newLog