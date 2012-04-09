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


if __name__ == "__main__":
	from bars import vuBarsEffect
	from fire import fireEffect
	from scroll import scrollImage, scrollText, scrollSequence
	from multiEffect import multiEffect

	text = "Novation Launchpad is a 64 button 'music controller' that enables you to make music or mix tracks by other artists. You don't need advanced musical knowledge, just your own creativity."
	while 1:
		im = runEffect(scrollText(text,im),100)
		im = runEffect(fireEffect(im,100),100)
		im = runEffect(scrollSequence([im,Image.open("images/novation-launchpad.png")]))
		im = runEffect(multiEffect(im, [
			( vuBarsEffect(), (0,0,9,9) ),
			( scrollText(text, Image.new('RGB',(42,9))), (11,0,53,9) ),
			( vuBarsEffect(), (55,0,64,9) ),
		]))
