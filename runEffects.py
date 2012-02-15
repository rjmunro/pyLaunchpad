#!/usr/bin/env python
import Image
import launchpadPil

def scrollImage(im):
	while im.size[0]>0:
		im = im.crop((1,0)+im.size)
		yield(im)
	yield False

def runEffect(ef, count = 10000):
	while count!=0:
		im = ef.next()
		if not im:
			break
		launchpadPil.drawImage(im.crop((0,0,31,20)))
		count -= 1

if __name__ == "__main__":
	from bars import vuBarsEffect
	from fire import fireEffect
	while 1:
		runEffect(scrollImage(Image.open("images/novation-launchpad-2line.png")))
		runEffect(vuBarsEffect(),100)
		runEffect(fireEffect(Image.new('RGB',(31,20))),100)
