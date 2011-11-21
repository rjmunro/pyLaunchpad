#!/usr/bin/env python2.7
import launchpad
import time

if __name__=="__main__":
	launchPads = launchpad.findLaunchpads()
	l = launchpad.launchpad(*launchPads[0])

	l.reset()
	l.ledTest(1)
	l.setDrumRackMode()


	for y in range(9):
		for x in range(9):
			l.light(x,y,3,0)
	for y in range(9):
		for x in range(9):
			l.light(x,y,0,3)
	for y in range(9):
		for x in range(9):
			l.light(x,y,3,3)
	for y in range(9):
		for x in range(9):
			l.light(x,y,3,0)
	for y in range(9):
		for x in range(9):
			l.light(x,y,0,3)
	for y in range(9):
		for x in range(9):
			l.light(x,y,3,3)

	time.sleep(1)
