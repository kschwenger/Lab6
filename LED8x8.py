#LED8x8 class

from time import sleep
from shifter import Shifter # extend by composition


class LED8x8():
  'Class for controlling an array of LEDs'

  #pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]
  #pattern = [0b10000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
  
  def display(self, pattern): # display given part of a pattern
    #while True:
      for row in range(len(pattern)):
        self.shifter.shiftByte(~pattern[row]) # load the row values
        self.shifter.shiftByte(1 << (7 - row)) # select the given row
        self.shifter.ping(self.shifter.latchPin)
        sleep(0.001)
