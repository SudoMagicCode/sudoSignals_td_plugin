'''WSConnection
Interface for establishing connection and communication with Websocket

-----------------------------------------------------------------------------------------
Copyright (C) 2019 Ian Shelanskey - All Rights Reserved
-----------------------------------------------------------------------------------------
'''


import json
import time

#GLOBALS
HEARTBEAT_TIMER		= op('timer1_HeartBeat')
PINGTIMEOUT_TIMER	= op('timer2_PingTimeout')
WEBSOCKET 			= op('websocket1')
CONFIG_FILE			= op('filein1')

class WSConnection:
	'''Interface for maintaining connection and communication with remote websocket. 
	'''
	def __init__(self):
		self.API = mod('api').EXPORTS
		self.Config = tdu.Dependency({})
		self.LastPing = tdu.Dependency(0)
		self.LastPong = tdu.Dependency(0)
		self.AttemptReconnect = tdu.Dependency(0)
		self.Connected = False
		self.FirstPong = True
		
		self.RefreshConfig()
		
		HEARTBEAT_TIMER.par.start.pulse()
		return

	def RefreshConfig(self):
		latest = json.loads( CONFIG_FILE.text )
		self.Config.val = latest
		self.Config.modified()
		return

	def ParseMessage(self, message):
		'''Parses incoming messages for types that exist in API
		'''
		data = json.loads(message)
		if 'type' in data:
			messageType = data['type']
			if messageType in self.API:
				self.API[messageType](messageType, data['message'], data['data'])

		return

	def Send(self, data):
		'''Sends message back to server. arg[1] MUST be python dict.
		'''
		WEBSOCKET.sendText(json.dumps(data))
		return

	def HeartBeat(self):
		'''Sends ping and checks if connection still open.
		'''
		self.LastPing.val = time.time()*1000
		PINGTIMEOUT_TIMER.par.start.pulse()
		return

	def RecvPong(self):
		'''Util function to maintain connection.
		Restarts the heartbeat timer to ping again in 10 secs.
		'''
		if self.FirstPong:
			self.FirstPong = False
			self.FirstMessage()
		self.LastPong.val = time.time()*1000
		PINGTIMEOUT_TIMER.par.initialize.pulse()
		self.Connected = True
		HEARTBEAT_TIMER.par.start.pulse()
		return

	def PingTimeout(self):
		'''Util function to maintain connection.
		Called from timer2 when we miss a pong. This will trigger the reconnect sequence.
		'''
		self.AttemptReconnect.val = 1
		self.Connected = False
		self.FirstPong = True
		return

	def AttemptedReconnect(self):
		'''Util function to maintain connection.
		Called after reconnect sequence. Will attempt to ping server again. 
		'''
		self.AttemptReconnect.val = 0
		self.HeartBeat()
		return
		
	def TryPing(self):
		'''Util function to maintain connection.
		Had to separate ping from heart beat to prevent handshake interruptions. 
		'''
		WEBSOCKET.sendPing()
		return

	def FirstMessage(self):
		self.Send({"type": "open"})