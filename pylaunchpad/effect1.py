#!/usr/bin/env python2.7
import launchpad
import time
import random

if __name__=="__main__":
	launchPads = launchpad.findLaunchpads()
	launchPadObjs = []
	for l in launchPads:
		launchPadObjs.append(launchpad.launchpad(*l))
		launchPadObjs[-1].setDrumRackMode()

	#l.reset()
	#l.ledTest(1)

	while 1:
		x = random.randint(0, 8)
		y = random.randint(0, 8)

		r = int((x+time.time())*3/8)%4
		g = int((y+time.time())*3/8)%4

		launchPadObjs[0].light(x,y,r,g)
		launchPadObjs[1].light(x,8-y,r,g)
		launchPadObjs[2].light(8-x,y,r,g)
		launchPadObjs[3].light(8-x,8-y,r,g)
		time.sleep(0.001)
