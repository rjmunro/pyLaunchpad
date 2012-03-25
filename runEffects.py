#!/usr/bin/env python
import Image
from launchpadCollection import LaunchpadCollection

launchpads = LaunchpadCollection(3,2)

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
	from scroll import scrollImage, scrollText
	while 1:
		im = Image.new('RGB',(32,20))
		im = runEffect(scrollText("Novation Launchpad is a 64 button 'music controller' that enables you to make music or mix tracks by other artists. You don't need advanced musical knowledge, just your own creativity."),100)
		im = runEffect(scrollImage(Image.open("images/novation-launchpad-2line.png")))
		im = runEffect(vuBarsEffect(),100)
		im = runEffect(fireEffect(im),100)
