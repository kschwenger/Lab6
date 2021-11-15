from time import sleep
from LED8x8 import LED8x8
from random import randint

dataPin, latchPin, clockPin = 18, 19, 26



x = randint(0, 7) #random starting position
y = randint(0, 7)

while True:
  theLED8x8 = LED8x8(dataPin, latchPin, clockPin, 'p')
  
  theLED8x8.display()  #display the pattern on the led array

  if x < 1: #prevent position from going outside of 8x8
    x += randint(0,1)
  elif x > 6:  
    x += randint(-1,0)
  else: #random step
    x += randint(-1,1)
  
  if y < 1:
    y += randint(0,1)
  elif y > 6:
    y += randint(-1,0)
  else:
    y += randint(-1,1)
  
  theLED8x8.pattern[y] = 1 << x #change the yth row to be x

  sleep(.1)
#try with multi