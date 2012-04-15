#!/usr/bin/env python
import Image
from launchpadCollection import LaunchpadCollection

from bars import vuBarsEffect
from fire import fireEffect
from scroll import scrollImage, scrollText, scrollSequence
from multiEffect import multiEffect

launchpads = LaunchpadCollection(6,1)
im = Image.new('RGB', launchpads.getTotalSize())

class launchpadException(Exception):
	def __init__(self, value, line='unknown'):
		self.value = value + " at line %s" % line
	def __str__(self):
		return repr(self.value)

def runEffect(ef, count = 10000):
	while count!=0:
		try:
			im = ef.next().crop((0,0)+launchpads.getTotalSize())
		except StopIteration:
			break
		launchpads.drawImage(im)
		launchpads.poll()
		count -= 1
	return im

def parseInstructions(lines, im):
	lineNo = 0
	for line in lines:
		lineNo += 1
		line = line.strip()
		if not line or line[0]=='#':
			# Skip blank lines and comments
			continue
		try:
			effect, parameter = line.split(':',1)
		except ValueError:
			raise launchpadException("No colon",lineNo)
		if effect=="text":
			im = runEffect(scrollText(parameter,im))
		elif effect=="fire":
			if not parameter.isdigit():
				raise launchpadException("Fire effect takes a number", lineNo)
			im = runEffect(fireEffect(im,100),100)
		elif effect=="bars":
			if not parameter.isdigit():
				raise launchpadException("Bars effect takes a number", lineNo)
			im = runEffect(multiEffect(im, [
					( vuBarsEffect(), (0,0,9,9) ),
					( vuBarsEffect(), (11,0,20,9) ),
					( vuBarsEffect(), (22,0,31,9) ),
					( vuBarsEffect(), (33,0,42,9) ),
					( vuBarsEffect(), (44,0,53,9) ),
					( vuBarsEffect(), (55,0,64,9) ),
			]),int(parameter))
		elif effect=="textfire":
			im = runEffect(multiEffect(im, [
					( fireEffect(Image.new('RGB', (9,9))), (0,0,9,9) ),
					( scrollText(parameter, Image.new('RGB',(42,9))), (11,0,53,9) ),
					( fireEffect(Image.new('RGB', (9,9))), (55,0,64,9) ),
			]))
		elif effect=="textbars":
			im = runEffect(multiEffect(im, [
					( vuBarsEffect(), (0,0,9,9) ),
					( scrollText(parameter, Image.new('RGB',(42,9))), (11,0,53,9) ),
					( vuBarsEffect(), (55,0,64,9) ),
			]))
		elif effect=="image":
			scrolledImage = Image.open('images/'+parameter)
			im = runEffect(scrollSequence([im,scrolledImage,im]),1000)
		else:
			raise launchpadException("Unknown effect", lineNo)

def checkForFiles():
	found = False
	import os,shutil,sys
	thisFolder = os.path.dirname(os.path.abspath(__file__))
	mountFolder = "/media/"
	try:
		volumes = os.listdir(mountFolder)
		print volumes
		for vol in volumes:
			if os.path.exists(mountFolder + vol + "/sign.txt"):
				shutil.copy(mountFolder + vol + "/sign.txt", thisFolder + "/sign.txt")
				print "Copied from %s to %s" % (mountFolder + vol + "/sign.txt", thisFolder + "/sign.txt")
				found = True
			if os.path.exists(mountFolder + vol + "/launchpadImages"):
				images = os.listdir(mountFolder + vol + "/launchpadImages")
				for image in images:
					shutil.copy(mountFolder + vol + "/launchpadImages/" + image, thisFolder + "/images/" + image)
					print "Copied from %s to %s" % (mountFolder + vol + "/launchpadImages/" + image, thisFolder + "/images/" + image)
					found = True
	except:
		raise
		pass
	return found

if __name__ == "__main__":
	checkForFiles()

	lines = list(open("sign.txt",'r'))
	while 1:
		try:
			parseInstructions(lines,im)
		except launchpadException as e:
			im = runEffect(scrollText(str(e),im))
			raise
