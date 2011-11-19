#!/usr/bin/env python2.7
"""Python interface for Novation Launchpads

Requires pyPortMidi from http://alumni.media.mit.edu/~harrison/code.html
But that version doesn't compile on a modern python without patching.
"""

import pypm
import time

class LaunchPadError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def findLaunchpads():
	ins = []
	outs = []
	for loop in range(pypm.CountDevices()):
		interf,name,inp,outp,opened = pypm.GetDeviceInfo(loop)
		if name=="Launchpad":
			if inp:
				ins.append(loop)
			else:
				outs.append(loop)
	return zip(ins,outs)


class launchpad:
	midiIn = None
	midiOut = None
	drumrackMode = False

	def __init__(self, idIn, idOut):
		self.midiIn = pypm.Input(idIn)
		self.midiOut = pypm.Output(idOut, 0)

	def reset(self):
		self.midiOut.WriteShort(0xb0, 0, 0)

	def setDrumRackMode(self,drumrack=True):
		self.drumrackMode = drumrack
		self.midiOut.WriteShort(0xb0, 0, drumrack and 2 or 1)

	def light(self, x, y, red, green):
		if not 0 <= x <= 8: raise LaunchPadError("Bad x value %s" % x)
		if not 0 <= y <= 7: raise LaunchPadError("Bad y value %s" % y)
		if not 0 <= red <= 3: raise LaunchPadError("Bad red value %s" % red)
		if not 0 <= green <= 3: raise LaunchPadError("Bad green value %s" % green)

		if self.drumrackMode:
			if x==8:
				# Last column runs from 100 - 107
				note = 107-y;
			elif x<4:
				note = 36 + x + 4*y
			else:
				# Second half starts at 68, but x will start at 4
				note = 64 + x + 4*y
		else:
			note = x + 16*(7-y)
		velocity = 16*green + red + 8 + 4
		self.midiOut.WriteShort(0x90,note,velocity)

if __name__=="__main__":
	pypm.Initialize() # always call this first, or OS may crash when you try to open a stream
	launchPads = findLaunchpads()
	l = launchpad(*launchPads[0])

	l.reset()
	l.setDrumRackMode()

	for i in range(8):
		l.light(8,i,(i%2)*3,((i/2)%2)*3)

	for x in range(8):
		for y in range(8):
			l.light(x,y,x%4,y%4)
			time.sleep(.1)
			#l.light(x,y,0,3)
			print "%s%s" % (x,y),
		print

