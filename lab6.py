from time import sleep
from LED8x8 import LED8x8

dataPin, latchPin, clockPin = 18, 19, 26

theLED8x8 = LED8x8(dataPin, latchPin, clockPin)

while True:
  theLED8x8.display()
  sleep(0.001)