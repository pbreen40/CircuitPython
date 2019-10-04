import time
import pulseio
import board
import touchio
from adafruit_motor import servo
 
#imports all libraries 

touch_A0 = touchio.TouchIn(board.A0)  # A0touch on Metro M0 Express
touch_A4 = touchio.TouchIn(board.A4)  # A4 touch on Metro M0 Express
 
# create a PWMOut object on Pin A2
pwm = pulseio.PWMOut(board.A2, frequency=50)
# Create a servo object
moth_slippers = servo.ContinuousServo(pwm)
 
while True: #loops
    if touch_A0.value: #if wire is touched
        moth_slippers.throttle = 1.0 #rotate slowly forwards
        print("A0")
    if touch_A4.value: 
        moth_slippers.throttle = -1.0
        print("A4") #rotate slowly forwards
    if not touch_A0.value and not touch_A4.value:

        moth_slippers.throttle = 0.0
        # makes sure servo doesn't move when wires aren't touched
    time.sleep(0.1)