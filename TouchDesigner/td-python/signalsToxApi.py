import signalsErrors
import signalsTDPluginEXT
import logger
import packets

signalsService: signalsTDPluginEXT.SignalsClient = parent.signals.op(
    'base_core')


class signals:
    def __init__(self, ownerOp):
        self.Owner_op = ownerOp

    def Send_log(self, logLevel: str, logMessage: str) -> None:
        if logLevel not in logger.LOG_MAP_LOOKUP.keys():
            raise signalsErrors.LogError(
                f"{logLevel} is not a supported logLevel, please use {self.log_levels}")

        else:
            level: int = logger.LOG_MAP_LOOKUP.get(logLevel)
            print(signalsService)
            signalsService.SetLog(level, logMessage)
