import time
import board
from rgb import RGB   # import the RGB class from the rgb module

r1 = board.D3
g1 = board.D4
b1 = board.D5
r2 = board.D1
g2 = board.D2
b2 = board.D7

myRGB1 = RGB(r1,g1,b1)   # create a new RGB object, using pins 3, 4, and 5
myRGB2 = RGB(r2,g2,b2)   # create a new RGB object, using pins 8, 9, and 10

myRGB1.red()          # Glow red
myRGB2.green()        # Glow green
time.sleep(1)
myRGB1.blue()      # Glow blue
myRGB2.cyan()         # Glow... you get it...
time.sleep(1)
myRGB1.magenta()      # Did you know magenta isn't in the rainbow?
myRGB2.yellow()       # Like you learned in first grade, red and green make... huh?
time.sleep(1)
myRGB1.rainbow1() # Nicely fade through all the colors of the rainbow at the given rate.  Oooooh, pretty!
myRGB2.rainbow2() # Nicely fade through all the colors of the rainbow at the given rate.  Oooooh, pretty!
time.sleep(1)