#!/usr/bin/env python
import random
import Image
import ImageDraw
import ImageFont
import launchpadPil

STEPS = 8
LOOPS = 8

def getLevelsPil():
	levels = [random.randint(0,8) for i in range(9)]
	im = Image.new('RGB',(31,20))
	draw = ImageDraw.Draw(im)
	while 1:
		newLevels = [random.randint(0,8) for i in range(9)]
		for step in range(STEPS):
			draw.rectangle((0,0,33,20),fill=(0,0,0))
			averageLevels = [ a + ((b-a)*step)/STEPS for [a,b] in zip(levels,newLevels)]
			for i in range(len(averageLevels)):
				x1 = i*3 + i/3*2
				x2 = x1+1
				y2 = 20
				y1 = y2-averageLevels[i]
				draw.rectangle((x1,y1,x2,y2),fill=(0,255,0))
				if (y1<14):
					draw.rectangle((x1,y1,x2,13),fill=(255,0,0))
			yield im
		levels = newLevels

def fireEffect(im, loops = 200):
	(xsize,ysize) = im.size

	def color2temp((r,g,b)):
		return r + g + b

	def temp2color(temp):
		return (min(temp,255),min(max(temp-255,0),255),max(temp-511,0))
	
	while loops!=0:
		# Draw bottom row randomly
		for x in range(xsize):
			temp = random.randint(100,768)
			im.putpixel((x,ysize-1),(temp2color(temp)))

		# Draw all other rows by averaging those below
		for y in range(ysize-1):
			# Blank pixels at edge
			im.putpixel((0,y),(0,0,0))
			im.putpixel((xsize-1,y),(0,0,0))
			
			for x in range(1,xsize-2):
				a = im.getpixel((x-1,y+1))
				b = im.getpixel((x,y+1))
				c = im.getpixel((x+1,y+1))

				average = temp2color(sum([color2temp(i) for i in a,b,c])/3-(500/ysize))

				im.putpixel((x,y),tuple(average))

		yield im
		loops -= 1

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
	while 1:
		runEffect(scrollImage(Image.open("images/novation-launchpad-2line.png")))
		runEffect(getLevelsPil(),100)
		runEffect(fireEffect(Image.new('RGB',(31,20))),100)
