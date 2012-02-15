#!/usr/bin/env python
import Image
import launchpadPil

def runEffect(ef, count = 10000):
	while count!=0:
		try:
			im = ef.next()
		except StopIteration:
			break
		if not im:
			StopIteration
		launchpadPil.drawImage(im.crop((0,0,31,20)))
		count -= 1

if __name__ == "__main__":
	from bars import vuBarsEffect
	from fire import fireEffect
	from scroll import scrollImage, scrollText
	while 1:
		runEffect(scrollText("Novation Launchpad is a 64 button 'music controller' that enables you to make music or mix tracks by other artists. You don't need advanced musical knowledge, just your own creativity."))
		runEffect(scrollImage(Image.open("images/novation-launchpad-2line.png")))
		runEffect(vuBarsEffect(),100)
		runEffect(fireEffect(Image.new('RGB',(31,20))),100)
