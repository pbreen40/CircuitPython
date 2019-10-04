import board
import neopixel
#import math
import time
#import digitalio
#import adafruit_bus_device
import adafruit_hcsr04
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5) #sets pins
#simpleio.map_range(x, in_min, in_max, out_min, out_max)

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = .1)#sets up neopixel



r = 0
g = 0
b = 0
#sets rgb values to off

while True:

    try:
        print((sonar.distance,))
        if sonar.distance <= 20: #if within range run red sequence

            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 5,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        else: #run blue/green sequence
            r = simpleio.map_range(sonar.distance, 0,20,255,0)
            b = simpleio.map_range(sonar.distance, 35,20,0,255)
            g = simpleio.map_range(sonar.distance, 20,35,0,255)

        dot.fill((int(r),int(g),int(b))) #send rgb values to LED
    except RuntimeError:
        print("Error")





    time.sleep(0.1)