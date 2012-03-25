#!/usr/bin/env python
import random
import Image
import ImageDraw

# Amount of frames to spend going to destination before new random destination is picked.
STEPS = 8

def vuBarsEffect():
	levels = [random.randint(0,8) for i in range(9)]
	im = Image.new('RGB',(31,20))
	draw = ImageDraw.Draw(im)
	while 1:
		newLevels = [random.randint(0,8) for i in range(9)]
		for step in range(STEPS):
			# Clear image
			draw.rectangle((0,0,33,20),fill=(0,0,0))
			averageLevels = [ a + ((b-a)*step)/STEPS for [a,b] in zip(levels,newLevels)]
			for i in range(len(averageLevels)):
				x1 = i*3 + i/3*2
				x2 = x1+1
				y2 = 20
				y1 = y2-averageLevels[i]
				# Draw green bar
				draw.rectangle((x1,y1,x2,y2),fill=(0,255,0))
				if (y1<14):
					# Draw red peak
					draw.rectangle((x1,y1,x2,13),fill=(255,0,0))
			yield im
		levels = newLevels
