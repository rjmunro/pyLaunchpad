#!/usr/bin/env python2.7
# vim: set fileencoding=UTF-8 :
"""Novation Launchpad python interface emulator

Requires pyGame
"""

import pygame
pygame.init()

class LaunchpadError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)


class Launchpad:
	_window = None
	_xPos = None
	_yPos = None
	_size = 4
	_drumrackMode = False

	def __init__(self, window, xPos, yPos, size=4):
		self._window = window
		self._xPos = xPos
		self._yPos = yPos
		self._size = size

	def reset(self):
		self.ledTest(0)

	def ledTest(self, brightness):
		if not 0 <= brightness <= 3: raise LaunchpadError("Bad brightness value %s" % brightness)
		for x in range(9):
			for y in range(9):
				self.light(x,y,brightness,brightness)
		self._drumrackMode = False

	def setDutyCycle(self, numerator, denominator):
		pass

	def setDrumRackMode(self, drumrack=True):
		self._drumrackMode = drumrack

	def light(self, x, y, red, green):
		if not 0 <= x <= 8: raise LaunchpadError("Bad x value %s" % x)
		if not 0 <= y <= 8: raise LaunchpadError("Bad y value %s" % y)
		if not 0 <= red <= 3: raise LaunchpadError("Bad red value %s" % red)
		if not 0 <= green <= 3: raise LaunchpadError("Bad green value %s" % green)

		if x==8 and y==8:
			return

		color = (45 + red * 70, 45 + green * 70, 45)
		pos = (self._xPos + x*self._size*3, self._yPos + (8-y)*self._size*3)

		if y==8 or x==8: 
			pygame.draw.circle(self._window, color, pos, self._size)
		else: 
			pygame.draw.rect(self._window, color, (pos[0] - self._size,pos[1] - self._size, self._size*2, self._size*2))

	def lightAll(self, levels):
		for x in range(9):
			for y in range(9):
				self.light(x,y,levels[x][y][0],levels[x][y][1])

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



	def lightSingleTest(self):
		for x in range(8):
			for y in range(8):
				self.light(x,y,x%4,y%4)

	def lightAllTest(self,r=None,g=None):
		grid = []
		for x in range(9):
			grid.append([])
			for y in range(9):
				if (r==None):
					grid[x].append( (x%4, y%4) )
				else:
					grid[x].append( (r%4, g%4) )

		self.lightAll(grid)

	def poll(self):
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				exit()
			# TODO: check for clicks
		return None
	
	def showImage(self, im, offsetx=0, offsety=0):
		grid = []
		xsize,ysize = im.size
		for x in range(9):
			grid.append([])
			for y in range(9):
				r,g,b = im.getpixel(((x + offsetx) % xsize, (8-y + offsety) % ysize))[:3]
				grid[x].append((r/64, g/64))
		self.lightAll(grid)

def setup6():
	return setupMany(3,2)

def setupMany(xcount,ycount,size=4,xskip=2,yskip=1):
	xspacing = size * (27 + 3 * xskip)
	yspacing = size * (27 + 3 * yskip)
	(width, height) = (10+xcount*xspacing, 10+ycount*yspacing)
	screen = pygame.display.set_mode((width, height))

	start = 20
	launchpads = []
	for x in range(xcount):
		for y in range(ycount):
			launchpads.append(Launchpad(screen, start + x * xspacing, start + y * yspacing, size))

	for l in launchpads:
		l.reset()
	
	return launchpads

if __name__=="__main__":
	import time

	launchpads = setup6()

	pygame.display.flip()
	running = True
	while running:
		launchpads[0].poll()
