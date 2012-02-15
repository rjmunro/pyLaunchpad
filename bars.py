#!/usr/bin/env python
import random
import Image
import ImageDraw
import ImageFont

STEPS = 8
LOOPS = 5

def getLevelsPil():
	levels = [random.randint(0,8) for i in range(9)]
	im = Image.new('RGB',(31,20))
	draw = ImageDraw.Draw(im)
	for count in range(LOOPS):
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

def fireEffect(im):
	(xsize,ysize) = im.size

	# Draw bottom row randomly
	for x in range(xsize):
		temp = random.randint(100,512)
		red = min(temp,255)
		green = max(temp-255,0)
		im.putpixel((x,ysize-1),(red,green,0))

	# Draw all other rows by averaging those below
	for y in range(ysize-1):
		for x in range(1,xsize-2):
			a = im.getpixel((x-1,y+1))
			b = im.getpixel((x,y+1))
			c = im.getpixel((x+1,y+1))

			average = [sum(i)*5/17 for i in zip(a,b,c)]

			im.putpixel((x,y),tuple(average))

	return im


import launchpadPil
count = 0
im = Image.new('RGB',(31,20))
for i in range(1000):
	im = fireEffect(im)
	launchpadPil.drawImage(im)
text = Image.open("images/novation.png");
for im in getLevelsPil():
	count +=1
	im.paste(text,(30-count,0))
	launchpadPil.drawImage(im)


