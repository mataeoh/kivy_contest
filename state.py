from stateMachine import *

STATE_NONE = 0
STATE_RESET = 1
STATE_MIX = 2
STATE_PLAY = 3
STATE_COMPLETE = 4
STATE_FAIL = 5
STATE_COUNT = 6

gameState = stateMachine(STATE_COUNT)


class NumPuzzleGameBase():
	bFirstGame = True
	szDebug = None
	level_name = ['Beginner', 'Intermediate', 'Advanced', 'Expert']
	sound_wow = None
	current_source = None
	complete_picture = None
	fTime = 0.0
	buttonList = []
	lastButton = None
	moveButton1 = None
	moveButton2 = None
	level = 0
	icons = []
	sounds = {}
	mySound = None
	mixCount = 0
	numericCount = 0
	numericCols = 0
	numericRows = 0
	fFrameTime = 0.0
	vMoveVel = 100.0
	oldDir = -1
	curDir = -1
	
	def start(self):
		gameState.stateList[STATE_NONE].onEnter = self.stateNone_onEnter
		gameState.stateList[STATE_RESET].onEnter = self.stateReset_onEnter
		gameState.stateList[STATE_MIX].onEnter = self.stateMix_onEnter
		gameState.stateList[STATE_MIX].onUpdate = self.stateMix_onUpdate
		gameState.stateList[STATE_PLAY].onEnter = self.statePlay_onEnter
		gameState.stateList[STATE_PLAY].onUpdate = self.statePlay_onUpdate
		gameState.stateList[STATE_COMPLETE].onEnter = self.stateComplete_onEnter
		gameState.stateList[STATE_COMPLETE].onUpdate = self.stateComplete_onUpdate
		gameState.set_state(STATE_NONE)
	
	def buildNumeric(self, cols=0, rows=0):
		pass
		
	def mixNumeric(self):
		pass
		
	def switchButton(self, btn1, btn2, bNow):
		pass
	
	def setMoveButton(self, btn1, btn2):
		pass
		
	def updateMoveButton(self):
		pass
				
	def checkComplete(self):
		pass

	# states
	def stateReset_onEnter(self):
		pass
		
	def stateMix_onEnter(self):
		pass
		
	def stateMix_onUpdate(self):
		pass
	
	def statePlay_onEnter(self):
		pass
		
	def statePlay_onUpdate(self):
		pass

	def stateComplete_onEnter(self):
		pass

	def stateComplete_onUpdate(self):
		pass