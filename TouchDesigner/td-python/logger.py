import utils
import packets
import SudoSignals

LOG_MAP_LOOKUP: dict['str', 'int'] = {
    "LOG": 0,
    "INFO": 1,
    "WARN": 2,
    "CRIT": 3,
    "ALERT": 4
}
LOG_LEVEL_LOOKUP: dict['str': SudoSignals.signalsLogLevel] = {
    '0': SudoSignals.signalsLogLevel.LOG,
    '1': SudoSignals.signalsLogLevel.INFO,
    '2': SudoSignals.signalsLogLevel.WARN,
    '3': SudoSignals.signalsLogLevel.CRIT,
    '4': SudoSignals.signalsLogLevel.ALERT
}


class SignalsLogger:

    def __init__(self):
        self.__logTables = []
        return

    def CreateLog(self, logLvl: int, logMsg: str) -> packets.logs.Log:
        newLog = None

        valid_log_lvl = [0, 1, 2, 3, 4]
        log_level_map = [
            SudoSignals.signalsLogLevel.LOG,
            SudoSignals.signalsLogLevel.INFO,
            SudoSignals.signalsLogLevel.WARN,
            SudoSignals.signalsLogLevel.CRIT,
            SudoSignals.signalsLogLevel.ALERT
        ]
        if logLvl not in valid_log_lvl:
            print(utils.Text_port_msg(
                'WARN', 'Incorrect Log Level || Log level should be a value of 0, 1, 2, 3, 4'))
        else:
            newLog = packets.logs.Log()
            newLog.level = log_level_map[logLvl]
            newLogMessage = packets.log_fields.LogMessage(value=logMsg)
            newLog.message.CopyFrom(newLogMessage)
        return newLog

    def CreateLogFromTable(self, logOp: op) -> packets.logs.Log:
        newLog = None

        # check to ensure op is table
        if logOp.type != 'table':
            print(utils.Text_port_msg(
                'WARN', 'Incorrect Log Op Type || Operator type should be TableDAT'))
        else:
            # check to ensure table DAT is the correct size
            if logOp.numCols != 2 and logOp.numRows != 2:
                print(utils.Text_port_msg(
                    'WARN', 'Incorrect Table Size || Table DAT should be 2 x 2'))
            else:
                # check to ensure log level is valid entry
                if logOp[0, 1].val not in LOG_LEVEL_LOOKUP.keys():
                    print(utils.Text_port_msg(
                        'WARN', 'Incorrect Log Level || Log level should be a value of 0, 1, or 2'))
                else:
                    newLog = packets.logs.Log()
                    newLog.level = LOG_LEVEL_LOOKUP[logOp[0, 1].val]
                    newLogMessage = packets.log_fields.LogMessage(
                        value=logOp[1, 1].val)
                    newLog.message.CopyFrom(newLogMessage)

        return newLog
