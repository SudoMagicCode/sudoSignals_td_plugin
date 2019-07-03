'''API for WSConnection
Here is where we define the interfaces for responding to server requests.


-----------------------------------------------------------------------------------------
Copyright (C) 2019 Ian Shelanskey - All Rights Reserved
-----------------------------------------------------------------------------------------

Functions defined within this file can be exported to the WSConnection by
appending them to the dictionary at the bottom of the file. The exported
function will be called when a message is received from the Websocket with
the exported key.

Example - When WSConnection receives a message with the "type" parameter "info"
the Info function (shown below) is called with the following arguments:
	messageType: 	string 	- the type of message sent from server
	message: 		string 	- a message assocaited, generally a human readable intention
	data: 			any 	- the payload of the message
	options: 		any 	- this is most likely a dictionary containing optional info

These arguments are REQUIRED for any custom API calls. 

-----------------------------------------------------------------------------------------
Response API

You can send back to the server using parent().Send(msg)

The message MUST be passed as a dictionary key two required keys:
	type: 		string	- the type of message
	message:	string	- a human readable message noting the intention of the message

'''
def Info(messageType, message, data, options=None):
	# This interface acknowledges the servers info message. 
	doc = {"type": "info", "message": "Ack"}
	parent().Send(doc)
	return
	
	
# Append any additional exports to this dictionary using the appropriate type expected from server. 
EXPORTS = {
	"info": Info
}