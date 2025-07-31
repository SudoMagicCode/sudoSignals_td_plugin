import SudoSignals
import signalsErrors
import utils
import json


class signalsClient(SudoSignals.signalsInterface):

    def __init__(self, ownerOp):
        self.signalsManager = SudoSignals.signalsManager(interface=self)
        super().__init__()

        self.Owner_op = ownerOp
        self.websocket = ownerOp.op('websocket_signals')
        self.report_timer = ownerOp.op('report_timer')
        self. default_custom_pars = ownerOp.op('base_default_custom_pars')
        self.signalsReports = ownerOp.op('null_defaultReport')

        self.PARSignalsid = parent.signals.par.Signalsid
        self.PARSignalsName = parent.signals.par.Signalsname
        self.PARConnected = parent.signals.par.Connected
        self.PARControlcomp = parent.signals.par.Controlcomp
        self.PARStartupdelay = parent.signals.par.Startupdelay
        self.PARManualconfig = parent.signals.par.Manualconfig

        self._reset_websocket(self.websocket)

        # Set Product ID
        self._get_signals_id

        # Set Product Name
        self._get_signals_name

        print(utils.Text_port_msg('INFO', 'Signals EXT Init'))
        # self.SetLog(0, '[*] :: SudoSignals TouchDesigner Plugin Initialized')

    @property
    def _get_signals_id(self):
        """Updates Signals ID - both member and par

        Args
        ----------
        None

        Returns
        ----------
        signalsId (str)
        > signals ID string retrieved from the signals env var
        """

        if self.PARManualconfig.eval():
            signalsId = self.PARSignalsid.eval()

        else:
            try:
                signalsId = me.var('SIGNALS_ID')
            except:
                signalsId = 'no_id_assigned'

        self.PARSignalsid.val = signalsId
        self.Id = signalsId
        return signalsId

    @property
    def _get_signals_name(self):
        """Updates Signals Name - both member and par

        Args
        ----------
        None

        Returns
        ----------
        signalsName (str)
        > signals Name string retrieved from the signals env var
        """

        try:
            signalsName = me.var('SIGNALS_NAME')
        except:
            signalsName = 'no_name_assigned'

        self.PARSignalsName.val = signalsName
        self.Name = signalsName
        return signalsName

    @property
    def par_signals_name(self):
        return self.PARSignalsName.eval()

    @property
    def par_signals_id(self):
        return self.PARSignalsid.eval()

    @property
    def par_connected(self):
        return self.PARConnected.eval()

    @property
    def par_control_comp(self):
        return self.PARControlcomp.eval()

    @property
    def par_reports1(self):
        return self.PARReports1.eval()

    @property
    def par_startup_delay(self):
        return self.PARStartupdelay.eval()

    @property
    def has_valid_signals_id(self):
        return True if self.Id is not None else False

    def Update_connected(self, state):
        self.PARConnected.val = state

    def Signals_start_up(self):
        """Signals Start-up Sequence

        Ensures signals start up is consistent, and reliable.
        Waits to send control updates until 60 frames have passed. This
        Should ensure that we've completed any necessary start-up and
        initialization elements

        Args
        ----------
        None

        Returns
        ----------
        None
        """
        print('-'*20)
        print(utils.Text_port_msg('INFO', 'Starting TD Client'))
        print('-'*20)

        self._reset_websocket(self.websocket)

        # Start connection here.
        self.websocket.par.active = 1

        # Send control-Set packet.
        startUpDelayControls = 'args[0].SetControls()'
        run(startUpDelayControls, self, delayFrames=self.par_startup_delay)

        # Start Sending Reports.
        self.Send_report()
        self.report_timer.par.start.pulse()

    def Clean_up(self) -> None:
        self._clean_up()

    def _clean_up(self) -> None:
        parent.signals.par.Connected = False

    def Restart_connection(self) -> None:
        self._reset_websocket(self.websocket)

    def _reset_websocket(self, websocket: callable) -> None:
        websocket.par.reset.pulse()

    def Send_log(self, log: SudoSignals.signalsLog) -> None:

        if log == None:
            print(utils.Text_port_msg('WARN', 'Log suppressed - Nonetype received'))

        else:
            self.signalsManager.sendLog(log)

    def Send_log_from_table_update(self, logOp) -> None:
        """Sends log info to SudoSignals Desktop Service
        """

        newLog = self._create_log_from_table(logOp)
        self.Send_log(newLog)

        # clear message
        logOp[1, 1] = ''

    def Create_log(self, logLevel: int, logMessage: str) -> SudoSignals.signalsLog:
        '''
        '''
        log_level = utils.LOG_LEVEL_LOOKUP.get(
            str(logLevel), SudoSignals.signalsLogLevel.INFO)
        log_message = logMessage
        new_log = SudoSignals.signalsLog(
            logLevel=log_level, message=log_message)

        return new_log

    def _create_log_from_table(self, logOp) -> SudoSignals.signalsLog:
        '''
        '''

        # check to ensure op is table
        if logOp.type != 'table':
            raise signalsErrors.LogError(
                'Incorrect Log Op Type || Operator type should be TableDAT')

        else:
            # check to ensure table DAT is the correct size
            if logOp.numCols != 2 and logOp.numRows != 2:
                raise signalsErrors.LogError(
                    'Incorrect Table Size || Table DAT should be 2 x 2')

            else:
                # check to ensure log level is valid entry
                if logOp[0, 1].val not in utils.LOG_LEVEL_LOOKUP.keys():
                    raise signalsErrors.LogError(
                        f'Incorrect Log Level || Log level should be a value of {utils.LOG_LEVEL_LOOKUP.keys()}')

                else:
                    log_level = utils.LOG_LEVEL_LOOKUP[logOp[0, 1].val]
                    log_message = logOp[1, 1].val
                    new_log = SudoSignals.signalsLog(
                        logLevel=log_level, message=log_message)

        return new_log

    def Send_report(self, report: SudoSignals.signalsReport):
        '''
        '''
        self.signalsManager.send_report(report)

    def Set_controls(self) -> None:
        '''
        '''
        ...

    def Send_controls(self) -> None:
        '''
        '''
        ...

#    def __init__(self):

#         # Add Action Routes to hand incoming messages.
#         self.AddActionRoute("PROCESS_CONTROLS", self.UpdateControls)

#         # Setup Reporting
#         self.AddReportable(self.signalsReports)


#     def SetControls(self):
#         """Sends control-Set packet to SudoSignals Desktop Service
#         """

#         # controlState = self.CreateControls()
#         # newControlPacket = {
#         #    "action": "control-Set",
#         #    "data": {"state": controlState}
#         # }

#         controlPages = self.CreateControls()
#         newControlPacket = packets.CreateControlPacket(controlPages)
#         self.SendMessage(newControlPacket)

#     def SetLogFromTable(self, LogOp: op) -> None:
#         """Sends log info to SudoSignals Desktop Service
#         """

#         newLog = self.CreateLogFromTable(LogOp)
#         self.SendLog(newLog)

#         # clear message
#         LogOp[1, 1] = ''

#     def UpdateControls(self, packet: packets.websockets_packets.WebsocketPacket):
#         updatedControl = packets.controls.Control()
#         packet.payload.Unpack(updatedControl)

#         self.UpdateControlComp(updatedControl)
