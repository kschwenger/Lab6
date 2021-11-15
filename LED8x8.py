#LED8x8 class
import multiprocessing
from time import sleep
from shifter import Shifter # extend by composition


class LED8x8(multiprocessing.Process):
  'Class for controlling an array of LEDs'
  
  pattern = multiprocessing.Array('i',[0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000])  #start empty

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
    p = multiprocessing.Process(target=self.display, args=(self.pattern,))
    p.daemon = True
    p.start()

  
  def display(self, pattern): # display given part of a pattern
    #while True:
      for row in range(len(pattern)):
        self.shifter.shiftByte(~pattern[row]) # load the row values
        self.shifter.shiftByte(1 << (7 - row)) # select the given row
        self.shifter.ping(self.shifter.latchPin)
        sleep(0.001)
