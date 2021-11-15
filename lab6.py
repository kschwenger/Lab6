from time import sleep
from LED8x8 import LED8x8
from random import randint

dataPin, latchPin, clockPin = 18, 19, 26

theLED8x8 = LED8x8(dataPin, latchPin, clockPin)

pattern = [0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]  #start empty

x = randint(0, 7) #random starting position
y = randint(0, 7)

while True:
  pattern[y] = 1 << x #change the yth row to be x
  theLED8x8.display(pattern)

  x += randint(-1,1)
  y =+ randint(-1,1)
