#!/usr/bin/env python
import random
import Image
import ImageDraw

# Amount of frames to spend going to destination before new random destination is picked.
STEPS = 8

def vuBarsEffect(width=2, height=9, space=1, number=3):
	levels = [random.randint(0,height) for i in range(number)]
	im = Image.new('RGB',((width+space)*number,height))
	draw = ImageDraw.Draw(im)
	while 1:
		newLevels = [random.randint(0,height) for i in range(number)]
		for step in range(STEPS):
			# Clear image
			draw.rectangle((0,0)+im.size,fill=(0,0,0))
			averageLevels = [ a + ((b-a)*step)/STEPS for [a,b] in zip(levels,newLevels)]
			for i in range(len(averageLevels)):
				x1 = i*(width + space)
				x2 = x1 + width - 1
				y2 = height
				y1 = y2-averageLevels[i]
				# Draw green bar
				draw.rectangle((x1,y1,x2,y2),fill=(0,255,0))
				if (y1<2):
					# Draw red peak
					draw.rectangle((x1,y1,x2,1),fill=(255,0,0))
			yield im
		levels = newLevels
