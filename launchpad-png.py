#!/usr/bin/env python2.7
import launchpad
import time
import sys

if __name__=="__main__":
	launchPads = launchpad.findLaunchpads()
	l = launchpad.launchpad(*launchPads[0])

	l.reset()
	l.setDrumRackMode()

	import Image
	im = Image.open(sys.argv[1])
	xsize,ysize = im.size

    
	for startx in range(xsize-8):
		grid = []
		for x in range(9):
			grid.append([])
			for y in range(9):
				r,g,b = im.getpixel((x+startx,8-y))
				grid[x].append((r/64, g/64))

		l.lightAll(grid)
		time.sleep(.1)

	time.sleep(1)
