#!/usr/bin/env python
import time
from numpy.random import *

last = 0

def dice(n):
    if(n==1):
        setLed(9)
    if(n==2):
        setLed(4)
        setLed(8)
    if(n==3):
        setLed(4)
        setLed(9)
        setLed(8)
    if(n==4):
        setLed(2)
        setLed(4)
        setLed(6)
        setLed(8)
    if(n==5):
        setLed(2)
        setLed(4)
        setLed(6)
        setLed(8)
        setLed(9)
    if(n==6):
        setLed(2)
        setLed(1)
        setLed(8)
        setLed(4)
        setLed(5)
        setLed(6)

def setLed(n):
    with open('/dev/myled0','w') as f:
        print >> f, n

def resetLed():
    with open('/dev/myled0','w') as f:
        print >> f, "F"

def allLed():
    with open('/dev/myled0','w') as f:
        print >> f, O

if __name__ == '__main__':
    while 1:
        last = randint(1,7)
        for i in range(50):
            last = randint(1,7)
            dice(last)
            time.sleep(0.2)
            resetLed()

        for i in range(10):
            dice(last)
            time.sleep(0.05)
            resetLed()
            time.sleep(0.05)
        dice(last)
        time.sleep(5)
        resetLed()
