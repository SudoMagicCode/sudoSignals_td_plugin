class SignalsLogger:
    def __init__(self):
        self.__logTables = []
        return
    
    def CreateLog(self):
            newLog = {
                'logLevel' : '0, 1, 2 | info, warn, crit' ,
                'msg' : ''			
            }
            return newLog