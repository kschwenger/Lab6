#LEDarray class

from time import sleep
from shifter import Shifter # extend by composition


class LEDarray():
  'Class for controlling an array of LEDs'

  pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
  
  def display(self): # display given part of a pattern
    for row in range(8):
      self.shifter.shiftByte(~LEDarray.pattern[row]) # load the row values
      self.shifter.shiftByte(1 << (row-1)) # select the given row
      self.shifter.ping(self.shifter.latchPin)
      sleep(0.001)
