#!/usr/bin/env python2.7
import launchpad
import time
import sys
import Image

def showImage(im, offsetx=0, offsety=0):
	grid = []
	xsize,ysize = im.size
	for x in range(9):
		grid.append([])
		for y in range(9):
			r,g,b = im.getpixel(((x + offsetx) % xsize, (8-y + offsety) % ysize))[:3]
			grid[x].append((r/64, g/64))
	l.lightAll(grid)

if __name__=="__main__":
	launchPads = launchpad.findLaunchpads()
	l = launchpad.launchpad(*launchPads[0])

	l.reset()
	l.setDrumRackMode()

	im = Image.open(sys.argv[1])
	xsize,ysize = im.size

    
	for startx in range(max(xsize-8,1)):
		showImage(im, startx)
		time.sleep(.1)

	# Sleep to allow buffer to empty
	time.sleep(1)
