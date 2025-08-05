# me - this DAT
# dat - the DAT that received a message

def onConnect(dat):
    parent.service.ext.Signals.UpdateConnected(True)
    return

# me - this DAT
# dat - the DAT that received a message


def onDisconnect(dat):
    parent.service.ext.Signals.UpdateConnected(False)
    parent.service.ext.Signals.Restart_connection()
    return

# me - this DAT
# dat - the DAT that received a message
# rowIndex - the row number the message was placed into
# message - an ascii representation of the text
#
# Only text frame messages will be handled in this function.


def onReceiveText(dat, rowIndex, message):
    parent.service.ext.Signals.Receive_message(message)
    return


# me - this DAT
# dat - the DAT that received a message
# contents - a byte array of the message contents
#
# Only binary frame messages will be handled in this function.

def onReceiveBinary(dat, contents):
    parent.service.ext.Signals.Receive_binary(contents)
    return

# me - this DAT
# dat - the DAT that received a message
# contents - a byte array of the message contents
#
# Only ping messages will be handled in this function.


def onReceivePing(dat, contents):
    dat.sendPong(contents)  # send a reply with same message
    return

# me - this DAT
# dat - the DAT that received a message
# contents - a byte array of the message content
#
# Only pong messages will be handled in this function.


def onReceivePong(dat, contents):
    return


# me - this DAT
# dat - the DAT that received a message
# message - an ascii representation of the message
#
# Use this method to monitor the websocket status messages

def onMonitorMessage(dat, message):
    return
