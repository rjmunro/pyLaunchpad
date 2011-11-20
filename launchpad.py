#!/usr/bin/env python2.7
"""Python interface for Novation Launchpads

Requires pyPortMidi from http://alumni.media.mit.edu/~harrison/code.html
But that version doesn't compile on a modern python without patching.

TODO:
	LED double-buffering and flashing
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
	_midiIn = None
	_midiOut = None
	_drumrackMode = False

	def __init__(self, idIn, idOut):
		self._midiIn = pypm.Input(idIn)
		self._midiOut = pypm.Output(idOut, 0)

	def reset(self):
		self._midiOut.WriteShort(0xb0, 0, 0)
		self._drumrackMode = False

	def ledTest(self, brightness):
		if not 1 <= brightness <= 3: raise LaunchPadError("Bad brightness value %s" % brightness)
		self._midiOut.WriteShort(0xb0, 0, 124 + brightness)
		self._drumrackMode = False

	def setDutyCycle(self, numerator, denominator):
		if numerator < 9:
			data = (16 * (numerator - 1)) + (denominator - 3)
			self._midiOut.WriteShort(0xb0, 0x1e, data)
		else:
			data = (16 * (numerator - 9)) + (denominator - 3)
			self._midiOut.WriteShort(0xb0, 0x1f, data)

	def setDrumRackMode(self, drumrack=True):
		self._drumrackMode = drumrack
		self._midiOut.WriteShort(0xb0, 0, drumrack and 2 or 1)

	def light(self, x, y, red, green):
		if not 0 <= x <= 8: raise LaunchPadError("Bad x value %s" % x)
		if not 0 <= y <= 8: raise LaunchPadError("Bad y value %s" % y)
		if not 0 <= red <= 3: raise LaunchPadError("Bad red value %s" % red)
		if not 0 <= green <= 3: raise LaunchPadError("Bad green value %s" % green)

		velocity = 16*green + red + 8 + 4

		if y==8:
			if x != 8:
				note = 104 + x
				self._midiOut.WriteShort(0xb0,note,velocity)
			return

		if self._drumrackMode:
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

		self._midiOut.WriteShort(0x90,note,velocity)

	def lightAll(self, levels):
		velocity = 0
		for level in self._orderAll(levels):
			red = level[0]
			green = level[1]
			if velocity:
				velocity2 = 16*green + red + 8 + 4
				self._midiOut.WriteShort(0x92, velocity, velocity2)
				time.sleep(.001)
				velocity = 0
			else:
				velocity = 16*green + red + 8 + 4
		self.light(0,0,levels[0][0][0],levels[0][0][1])

	def _orderAll(self,levels):
		for y in range(8):
			for x in range(8):
				yield levels[x][7-y]
		x = 8
		for y in range(8):
			yield levels[x][7-y]

		y = 8
		for x in range(8):
			yield levels[x][y]

if __name__=="__main__":
	pypm.Initialize() # always call this first, or OS may crash when you try to open a stream
	launchPads = findLaunchpads()
	l = launchpad(*launchPads[0])

	l.reset()
	l.setDrumRackMode()

	for x in range(8):
		for y in range(8):
			l.light(x,y,x%4,y%4)
			time.sleep(.1)

