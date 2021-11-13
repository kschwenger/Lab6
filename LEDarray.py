#LEDarray class

from time import sleep
from shifter import Shifter

pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

class LEDarray():
  'Class for controlling an array of LEDs'

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
  
  def display(self):
    rows = [1,2,3,4,5,6,7,8] # change this value to pick which row the pattern appears on
    for row in range(len(rows)):
      self.shifter.shiftByte(~LEDarray.pattern[part]) # load the row values
      self.shifter.shiftByte(1 << (row-1)) # select the given row

dataPin, latchPin, clockPin = 18, 23, 24

theLEDarray = LEDarray(dataPin, latchPin, clockPin)

while True:
  theLEDarray.display()
  sleep(.001)
