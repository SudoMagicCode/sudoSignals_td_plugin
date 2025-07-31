import signalsErrors
import signalsTDPlugin
import utils

signalsService: signalsTDPlugin.signalsClient = parent.signals.op(
    'base_core')


class signals:
    def __init__(self, ownerOp):
        self.Owner_op = ownerOp

    def Send_log(self, logLevel: str, logMessage: str) -> None:
        if logLevel not in utils.LOG_MAP_LOOKUP.keys():
            raise signalsErrors.LogError(
                f"{logLevel} is not a supported logLevel, please use {self.log_levels}")

        else:
            level: int = utils.LOG_MAP_LOOKUP.get(logLevel)
            new_log = signalsService.Create_log(level, logMessage)
            signalsService.Send_log(level, new_log)
