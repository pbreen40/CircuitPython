import time
import pulseio
import board
import touchio
from adafruit_motor import servo
 
touch_A0 = touchio.TouchIn(board.A0)  # A0-A5 touch on Metro M0 Express
touch_A4 = touchio.TouchIn(board.A4)  # A0-A5 touch on Metro M0 Express
 
# create a PWMOut object on Pin A2
pwm = pulseio.PWMOut(board.A2, frequency=50)
# Create a servo object, mine's named "moth_slippers"
moth_slippers = servo.ContinuousServo(pwm)
 
while True:
    if touch_A0.value:
        moth_slippers.throttle = 1.0
        print("A0")
    if touch_A4.value:
        moth_slippers.throttle = -1.0
        print("A4")
    if not touch_A0.value and not touch_A4.value:
        # must use one if statement rather than two else
        # if else was used the statments would cancel out
        # making the A4 wire work but not the A0
        moth_slippers.throttle = 0.0
        # makes sure servo doesn't move when wires aren't touched
    time.sleep(0.1)