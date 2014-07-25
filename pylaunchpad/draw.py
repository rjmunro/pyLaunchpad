#!/usr/bin/env python2.7
import launchpad
import time
import random

if __name__=="__main__":
    ls = launchpad.findLaunchpads()
    l = ls[0]
    l = launchpad.launchpad(*l)
    l.setDrumRackMode()

    l.reset()
    #l.ledTest(1)

    time.sleep(1)

    color = (3, 0)
    colors = ((3, 0), (1, 0), (0, 3), (0, 1), (3, 3), (1, 1), (0, 0), (0, 0))

    for i, c in enumerate(colors):
        l.light(i, 8, c[0], c[1])
    def updcol(): l.light(7, 8, color[0], color[1])
    updcol()

    while 1:
        event = l.poll()
        if event:
            x, y, state = event
            if state:
                if y == 8:
                    if x < 7:
                        color = colors[x]
                        updcol()
                else:
                    l.light(x, y, color[0], color[1])
        else:
            time.sleep(0.05)
