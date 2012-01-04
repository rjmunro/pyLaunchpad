#!/usr/bin/env python2.7
import launchpadSim
import launchpad
import time
import sys
import Image

SIM = True

# Set up launchpads
if SIM:
	launchPadObjs = launchpadSim.setup6()
else:
	launchPads = launchpad.findLaunchpads()
	launchPadObjs = []
	for l in launchPads:
		launchPadObjs.append(launchpad.launchpad(*l))
		launchPadObjs[-1].reset()

def drawImage(im):
	xsize,ysize = im.size

	for startx in range(max(xsize-(11*len(launchPadObjs)/2)+3,1)):
		for padx in range(len(launchPadObjs) / 2):
			for pady in range(2):
				l = launchPadObjs[padx*2+pady]
				l.showImage(im, 11*padx + startx, 10*pady)
		launchPadObjs[0].poll()
		time.sleep(.1)

if __name__=="__main__":

	im = Image.open(sys.argv[1])

	drawImage(im)

	# Sleep to allow buffer to empty
	time.sleep(1)
