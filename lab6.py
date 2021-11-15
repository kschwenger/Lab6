from time import sleep
from LED8x8 import LED8x8

dataPin, latchPin, clockPin = 18, 19, 26

theLED8x8 = LED8x8(dataPin, latchPin, clockPin)

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

theLED8x8.display(pattern)
