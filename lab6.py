from time import sleep
from LEDarray import LEDarray

dataPin, latchPin, clockPin = 18, 19, 26

theLEDarray = LEDarray(dataPin, latchPin, clockPin)

#sequence = [7, 6, 7, 5, 3, 0, 7]

while True:
  for n in range(8):
    theLEDarray.display(n)
    sleep(0.001)