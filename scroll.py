#!/usr/bin/env python
import Image

def scrollImage(im, minwidth=0):
	while im.size[0]>minwidth:
		im = im.crop((1,0)+im.size)
		yield(im)
