from digitalio import DigitalInOut, Direction, Pull
import board
import time
switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
presses = 0
fread = True 
lread = True #variables used in logic
initial = time.monotonic() #sets initial time
while True:
    now = time.monotonic() #sets current time
    if now - initial == 4:  # If 4 elapses
        print("I have been interrupted", presses, "times.")
        initial = time.monotonic() #resets initial

    if switch.value: #logic so it doesn't repeat
        lread = True

    else:
        if fread == lread:
                presses +=1
                lread = not lread