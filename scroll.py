#!/usr/bin/env python
import Image

def scrollImage(im, minwidth=0):
	while im.size[0]>minwidth:
		im = im.crop((1,0)+im.size)
		yield(im)

def scrollSequence(sequence, minwidth=70):
	im = Image.new('RGB',(1,1))
	for i in sequence[1:]:
		xsize,ysize = im.size
		im = im.crop((0,0, xsize+i.size[0], max(i.size[1],ysize)))
		im.paste(i,(xsize,0))

		for j in scrollImage(im,minwidth):
			yield j
			im = j

def scrollText(text, minwidth=70):
	map = {
		"'":"quote",
		",":"comma",
		".":"stop",
	}
	sequence = []
	for i in text:
		if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
			sequence.append(Image.open("letters/%s.png" % i))
		elif i in map:
			sequence.append(Image.open("letters/%s.png" % map[i]))
		else:
			sequence.append(Image.open("letters/space.png"))

	return scrollSequence(sequence, minwidth)
