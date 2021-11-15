from time import sleep
from LED8x8 import LED8x8

dataPin, latchPin, clockPin = 18, 19, 26

theLED8x8 = LED8x8(dataPin, latchPin, clockPin)

theLED8x8.display()
