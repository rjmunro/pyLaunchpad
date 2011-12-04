#!/usr/bin/env python2.7
import launchpad
import time
import random

if __name__=="__main__":
	launchPads = launchpad.findLaunchpads()
	launchPadObjs = []
	for l in launchPads:
		launchPadObjs.append(launchpad.launchpad(*l))

	#l.reset()
	#l.ledTest(1)
	#l.setDrumRackMode()

	while 1:
		for l in launchPadObjs:
			x = random.randint(0, 8)
			y = random.randint(0, 8)
			r = random.randint(0, 3)
			g = random.randint(0, 3)

			l.light(x,y,r,g)
			l.poll()
