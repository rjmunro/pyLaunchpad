#!/usr/bin/env python2.7
import time
import sys

if __name__=="__main__":

	import Image
	im = Image.open(sys.argv[1])
	xsize,ysize = im.size

	letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

	startx = 0
	for x in range(xsize):
		split = True
		for y in range(ysize):
			r,g,b = im.getpixel((x,8-y))
			if r or g or b:
				split = False
				break
		if split:
			if x > (startx + 1):
				letter = letters.pop(0)
				print startx, x
				im.crop((startx,0,x,im.size[1])).save('letters/' + letter + '.png')
			startx = x


