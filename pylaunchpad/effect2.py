#!/usr/bin/env python2.7
import launchpad
import time
from math import *

if __name__=="__main__":
    launchPads = launchpad.findLaunchpads()
    launchPadObjs = []
    for l in launchPads:
        launchPadObjs.append(launchpad.launchpad(*l))
        launchPadObjs[-1].setDrumRackMode()
    #launchPadObjs[0].reset()
    im = [[(0,0) for x in range(8)] for y in range(8)]
    while 1:
        for x in range(9):
            for y in range(9):
                r = int(2+1.5*sin(0.7*x+0.2*y+5*time.time()))
                g = int(2+1.5*sin(0.3*x+0.6*y+4*time.time()+3*sin(0.2*x+time.time())))
                launchPadObjs[0].light(x,y,r,g)
        time.sleep(0.001)

