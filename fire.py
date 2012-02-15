#!/usr/bin/env python
import random

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
