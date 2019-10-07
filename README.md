# CircuitPython
## My CircuitPython assignments

### LEDFade:
#### Objective
Make a LED fades in and out.
#### Picture

#### Lessons
In this assignment we learned how to use our new metro board and how to use CircuitPython on Mu.


  

### ServoTouch:
#### Objective
A Servo moves right or left, depending on if a wire is touched, using Capacitive Touch.
#### Picture

#### Lessons
In this assignment we learned how to use Capacitive touch, and how to control servos CircuitPython. When you touch one of the wires, your finger discharges to it, which lets the Metro know that you touched it.  


### LCDButtonSwitch:
#### Objective
A switch determines if a counter is increased, or decreased when a button is pushed. The counter is displayed on a LCD screen.
#### Picture

#### Lessons
In this assignment we learned how to use LCD screens and switches / buttons on CircuitPython. We had to make two boolean variables along with some logic that made sure the button wouldn't count more than once if it was held down. We also had an issue with the LCD glitching sometimes, so we had it print nothing to reset it.  


### PhotoInterrupter:
#### Objective
Every 4 seconds, the number of times the photo interrupter has been interrupted is displayed.
#### Picture

#### Lessons
In this assignment we learned how to use photointerrupters on CircuitPython. We used the same logic as in the LCD Button switch to make sure that it wouldn't count more than once when it was interuppted. We also found out how similiar a photo interuppter and a button are coded. 


### DistanceSensor:
#### Objective
Determines the distance from an object, and lights up a LED accordingly.
#### Picture

#### Lessons
In this assignment we learned how to use distance sensors on CircuitPython, and the neopixel on our metro. We had to map the values of each variable(R, G, B) so it could smoothly fade through colors. 


### ClassesObjectsAndModules:
#### Objective
Uses a library I made, rgb, to run different led functions.
#### Picture

#### Lessons
In this assignment we learned how to use classes, objects, and modules on CircuitPython. It took a bit to understand how they worked, but once you get used to using the different functions its pretty easy. 


### hello_vs_code:
#### Objective
Learned how to use vs code.
#### Picture

#### Lessons
In this assignment we learned how to use Hello Vs Code instead of Mu to run CircuitPython.


### FancyLED:
#### Objective
Used classes and objects to control 6 LEDS with 4 functions.
#### Picture

#### Lessons
In this assignment we learned how to use classes and objects on Hello Vs Code to control LEDs. We orignally had 6 different variables for pins, but we figured out how to make it so each function controls them seperately with just three. 
#### Important Code
`FancyLED.py`
``` python
     def __init__(self, p1, p2, p3):
        self.fancy1 = digitalio.DigitalInOut(p1) #sets temp values for p1/2/3
        self.fancy2 = digitalio.DigitalInOut(p2)
        self.fancy3 = digitalio.DigitalInOut(p3)
        self.fancy1.direction = digitalio.Direction.OUTPUT #defines them as outputs
        self.fancy2.direction = digitalio.Direction.OUTPUT
        self.fancy3.direction = digitalio.Direction.OUTPUT  
```
`FancyLEDMain.py (main.py)`
```python
fancy1 = fancyled(board.D2,board.D3,board.D4) #defines different pins for each function
fancy2 = fancyled(board.D5,board.D6,board.D7)
```
This is the part of the code that that lets us shorten six LED variables to 3 LEDs, it uses "fancy1" and "fancy2" instead of just "fancy."