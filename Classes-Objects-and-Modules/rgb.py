import pulseio
import simpleio
import time

class RGB:
     kind = "color" # class variable shared by all instances

     # you don't need an __init__ method, but it is common for stuff that runs at instantiaion
     def __init__(self, r,g,b):
        self.r = pulseio.PWMOut(r, duty_cycle=0, frequency=1000)
        self.g = pulseio.PWMOut(g, duty_cycle=0, frequency=1000)
        self.b = pulseio.PWMOut(b, duty_cycle=0, frequency=1000)

     def addTrick(self, trick):
          self.tricks.append(trick)

     def red(self):
        print("red")
        self.r.duty_cycle = 0
        self.b.duty_cycle = 2 ** 16-1
        self.g.duty_cycle = 2 ** 16-1
     def green(self):
        print("green")
        self.r.duty_cycle = 2 ** 16-1
        self.b.duty_cycle = 2 ** 16-1
        self.g.duty_cycle = 0
     def blue(self):
        print("blue")
        self.r.duty_cycle = 2 ** 16-1
        self.b.duty_cycle = 0
        self.g.duty_cycle = 2 ** 16-1
     def magenta(self):
        print("magenta")
        self.r.duty_cycle = 0
        self.b.duty_cycle = 0
        self.g.duty_cycle = 2 ** 16-1
     def cyan(self):
        print("cyan")
        self.r.duty_cycle = 2 ** 16-1
        self.b.duty_cycle = 0
        self.g.duty_cycle = 0

     def yellow(self):
        print("yellow")
        self.r.duty_cycle = 0
        self.b.duty_cycle = 2 ** 16-1
        self.g.duty_cycle = 0
     def rainbow1(self):
        rate= 128
        #print("rainbow")
        #self.r.duty_cycle = 0
        #self.b.duty_cycle = 2 ** 16-1
        #self.g.duty_cycle = 2 ** 16-1
        for i in range (0, 2 ** 16, rate):
            self.r.duty_cycle = 0+i
            self.b.duty_cycle = 2 ** 16-1-i
            self.g.duty_cycle = 2 ** 16-1
        for i in range (0, 2 ** 16, rate):
            self.r.duty_cycle = 2 ** 16-1
            self.b.duty_cycle = 0+i
            self.g.duty_cycle = 2 ** 16-1-i
        for i in range (0, 2 ** 16, rate):
            self.r.duty_cycle = 2 ** 16-1-i
            self.b.duty_cycle = 2 ** 16-1
            self.g.duty_cycle = 0+i
     def rainbow2(self):
        rate= 64
        #print("rainbow")
        #self.r.duty_cycle = 0
        #self.b.duty_cycle = 2 ** 16-1
        #self.g.duty_cycle = 2 ** 16-1
        for i in range (0, 2 ** 16, rate):
            self.r.duty_cycle = 0+i
            self.b.duty_cycle = 2 ** 16-1-i
            self.g.duty_cycle = 2 ** 16-1
        for i in range (0, 2 ** 16, rate):
            self.r.duty_cycle = 2 ** 16-1
            self.b.duty_cycle = 0+i
            self.g.duty_cycle = 2 ** 16-1-i
        for i in range (0, 2 ** 16, rate):
            self.r.duty_cycle = 2 ** 16-1-i
            self.b.duty_cycle = 2 ** 16-1
            self.g.duty_cycle = 0+i

