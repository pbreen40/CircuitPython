from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
import board
import time
import digitalio
from lcd.lcd import CursorMode
switch = DigitalInOut(board.D2)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
switch2 = DigitalInOut(board.D7)
switch2.direction = Direction.INPUT
switch2.pull = Pull.UP
# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
presses = 0
fread = True
while True:
    lcd.set_cursor_pos(0, 0) #sets cursor in proper position
    lcd.print("SwitchState:")
    if switch.value:
        fread = True #logic so it doesn't repeat
    else:
        if fread == True:
            if switch2.value:
                lcd.print("Up")
                lcd.print("    ") #spacer so it doesn't break
                presses +=1
                fread = not fread #resets fread
            else:
                lcd.print("Down")
                lcd.print("    ")
                presses -=1
                fread = not fread #resets fread
    lcd.set_cursor_pos(1, 0) #print everything needed
    lcd.print("Presses:")
    lcd.print(str(presses))#converts to string so it doesn't throw errors
    lcd.print("    ")
    lcd.cursor = False