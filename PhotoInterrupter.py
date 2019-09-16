from digitalio import DigitalInOut, Direction, Pull
import board
import time
switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
presses = 0
fread = True
lread = True
initial = time.monotonic()
while True:
    now = time.monotonic()
    if now - initial == 4:  # If 3 milliseconds elapses
        print("I have been interrupted", presses, "times.")
        initial = time.monotonic()

    if switch.value:
        lread = True

    else:
        if fread == lread:
                presses +=1
                lread = not lread