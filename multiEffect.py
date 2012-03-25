import ImageDraw

def multiEffect(im,effects):
	while 1:
		try:
			for effect in effects:
				nextIm = effect[0].next()
				bbox = effect[1]
				#mask = nextIm.convert('L').point(lambda x : x != 0 ,'1')
				nextIm = nextIm.crop((0,0,bbox[2]-bbox[0],bbox[3]-bbox[1]))
				im.paste(nextIm, effect[1])
		except StopIteration:
			break

		yield im
