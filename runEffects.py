#!/usr/bin/env python
import Image
from launchpadCollection import LaunchpadCollection

launchpads = LaunchpadCollection(6,1)
im = Image.new('RGB', launchpads.getTotalSize())

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
	from bars import vuBarsEffect
	from fire import fireEffect
	from scroll import scrollImage, scrollText, scrollSequence
	from multiEffect import multiEffect

	lineNo = 0
	for line in lines:
		lineNo += 1
		line = line.strip()
		if not line or line[0]=='#':
			# Skip blank lines and comments
			continue
		effect, parameter = line.split(':',1)
		if effect=="text":
			im = runEffect(scrollText(parameter,im))
		elif effect=="fire":
			if not parameter.isdigit():
				error("Fire effect takes a number")
			im = runEffect(fireEffect(im,100),100)
		elif effect=="bars":
			if not parameter.isdigit():
				error("Bars effect takes a number")
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
			#TODO: Check if image exists, check /media/ if it doesn't
			scrolledImage = Image.open('images/'+parameter)
			im = runEffect(scrollSequence([im,scrolledImage,im]),1000)
		else:
			error("Unknown effect on line %s" % lineNo)

if __name__ == "__main__":
	#TODO: Check for /media/*/sign.txt for and copy it to current folder

	lines = list(open("sign.txt",'r'))
	while 1:
		parseInstructions(lines,im)

