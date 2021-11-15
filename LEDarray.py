#LEDarray class

from time import sleep
from shifter import Shifter # extend by composition


class LEDarray():
  'Class for controlling an array of LEDs'

  pattern = [0b11111100, 0b01100000, 0b11011010, 0b11110010, 0b01100110, 0b10110110, 0b10111110, 0b11100000, 0b11111110, 0b11100110]
  #[0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
  
  def display(self, pat): # display given part of a pattern
    row = 7
    #rows = [1,2,3,4,5,6,7,8] # change this value to pick which row the pattern appears on
    #for row in range(len(rows)):
    self.shifter.shiftByte(~LEDarray.pattern[pat]) # load the row values
    self.shifter.shiftByte(1 << (row-1)) # select the given row
    self.shifter.ping(self.shifter.latchPin)
#trying to get it to do the same thing as example code but its not working