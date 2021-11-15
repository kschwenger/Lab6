from time import sleep
from LEDarray import LEDarray

dataPin, latchPin, clockPin = 18, 19, 26

theLEDarray = LEDarray(dataPin, latchPin, clockPin)

while True:
  #for n in range(8):
  theLEDarray.display()
    #sleep(0.001)