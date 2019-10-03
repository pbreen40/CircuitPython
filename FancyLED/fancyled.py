from board import *
import random
import digitalio
import simpleio
import time
class fancyled:
     kind = "color" # class variable shared by all instances

     # you don't need an __init__ method, but it is common for stuff that runs at instantiaion
     def __init__(self, p1, p2, p3):
        self.fancy1 = digitalio.DigitalInOut(p1)
        self.fancy2 = digitalio.DigitalInOut(p2)
        self.fancy3 = digitalio.DigitalInOut(p3)
        self.fancy1.direction = digitalio.Direction.OUTPUT
        self.fancy2.direction = digitalio.Direction.OUTPUT
        self.fancy3.direction = digitalio.Direction.OUTPUT

     def alternate(self):
        print("alternate")
        self.fancy1.value = True
        self.fancy2.value = False
        self.fancy3.value = True
        time.sleep(.15)
        self.fancy1.value = False
        self.fancy2.value = True
        self.fancy3.value = False
        time.sleep(.15)
     def blink(self):
        print("blink")
        time.sleep(.15)
        self.fancy1.value = False
        self.fancy2.value = False
        self.fancy3.value = False
        time.sleep(.15)
        self.fancy1.value = True
        self.fancy2.value = True
        self.fancy3.value = True
     def chase(self):
        print("chase")
        self.fancy1.value = True
        self.fancy2.value = False
        self.fancy3.value = False
        time.sleep(.15)
        self.fancy1.value = False
        self.fancy2.value = True
        self.fancy3.value = False
        time.sleep(.15)
        self.fancy1.value = False
        self.fancy2.value = False
        self.fancy3.value = True
        time.sleep(.15)
     def sparkle(self):
        print("sparkle")
        rand = random.randrange(4, 10, 1)
        uptime = random.randrange(0, 20, 1)
        uptime = uptime/150
       # print(uptime)
        if rand == 4:
           self.fancy1.value= True
           self.fancy2.value = False
           self.fancy3.value = False
           time.sleep(uptime)
        if rand == 5:
           self.fancy2.value= True
           self.fancy1.value = False
           self.fancy3.value = False
           time.sleep(uptime)
        if rand == 6:
           self.fancy3.value= True
           self.fancy1.value = False
           self.fancy2.value = False
           time.sleep(uptime)
        if rand > 6:
           self.fancy1.value = False
           self.fancy2.value = False
           self.fancy3.value = False
           time.sleep(uptime)

