from time import sleep
from LED8x8 import LED8x8
from random import randint

dataPin, latchPin, clockPin = 18, 19, 26  #define SR pins

theLED8x8 = LED8x8(dataPin, latchPin, clockPin) #create multiprocessing object

x = randint(0, 7) #random starting position (x = column, y = row)
y = randint(0, 7)

try:
  
  while True:
  
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
  
    for i in range(8):
      theLED8x8.pattern[i] = 0b00000000 #reset pattern to turn all LEDs off
    theLED8x8.pattern[y] = 1 << x #turn on xth bit in yth row 

    sleep(.1)
except Exception as e:   # catch everything, just in case
  theLED8x8.d.terminate()      # terminate the process
  theLED8x8.d.join(2)          # wait up to 2 sec for process termination before ending code
except KeyboardInterrupt: # if user hits ctrl-C
  print('\nExiting')