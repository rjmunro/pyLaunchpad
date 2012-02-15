#!/usr/bin/env python2.7
import launchpadSim
import launchpad
import time

class LaunchpadCollection:
	launchpadObjs = []
	xcount = 0
	ycount = 0
	xskip = 0
	yskip = 0

	def __init__(self, xcount, ycount, simSize=4, xskip=2, yskip=1):
		self.xcount = xcount
		self.ycount = ycount
		self.xskip = xskip
		self.yskip = yskip

		# Set up launchpads
		launchPads = launchpad.findLaunchpads()
		if launchPads:
			if len(launchPads) != xcount * ycount:
				print "Found %s launchpads, expecting %s" % (len(launchPads), xcount * ycount)
			for l in launchPads:
				self.launchPadObjs.append(launchpad.launchpad(*l))
				self.launchPadObjs[-1].reset()
		else:
			# Use simulator
			self.launchPadObjs = launchpadSim.setupMany(xcount, ycount, simSize, xskip, yskip)

	def drawImage(self, im):
		for padx in range(self.xcount):
			for pady in range(self.ycount):
				l = self.launchPadObjs[padx*self.ycount+pady]
				l.showImage(im, (9+self.xskip)*padx, (9+self.yskip)*pady)
		self.launchPadObjs[0].poll()
		time.sleep(.075)

