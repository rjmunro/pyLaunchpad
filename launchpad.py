#!/usr/bin/env python2.7
"""Python interface for Novation Launchpads

Requires pyPortMidi from http://alumni.media.mit.edu/~harrison/code.html
But that version doesn't compile on a modern python without patching.
"""

import pypm
import time

def findLaunchpads():
	ins = []
	outs = []
	for loop in range(pypm.CountDevices()):
		interf,name,inp,outp,opened = pypm.GetDeviceInfo(loop)
		print loop, name," ",
		print (inp == 1) and "(input) " or "(output) ",
		print (opened == 1) and "(opened)" or "(unopened)"
		if name=="Launchpad":
			if inp:
				ins.append(loop)
			else:
				outs.append(loop)
	print
	return zip(ins,outs)


class launchpad:
	midiIn = None
	midiOut = None
	def __init__(self, idIn, idOut):
		self.midiIn = pypm.Input(idIn)
		self.midiOut = pypm.Output(idOut, 0)

	def light(self, x, y, red, green):
		position = x+16*y
		color = 16*red + green + 8 + 4
		self.midiOut.WriteShort(0x90,position,color)

if __name__=="__main__":
	pypm.Initialize() # always call this first, or OS may crash when you try to open a stream
	launchPads = findLaunchpads()
	l = launchpad(*launchPads[0])
	print l,l.midiIn,l.midiOut
	for i in range(8):
		l.light(8,i,(i%2)*3,((i/2)%2)*3)

for x in range(8):
	for y in range(9):
		l.light(x,y,x%4,y%4)
		time.sleep(.03)
		l.light(x,y,0,0)
		print "%s%s" % (x,y),
	print

