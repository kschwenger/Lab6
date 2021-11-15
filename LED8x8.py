#LED8x8 class
import multiprocessing
from time import sleep
from shifter import Shifter 


class LED8x8(multiprocessing.Process):
  'Class for controlling an array of LEDs'
  
  pattern = multiprocessing.Array('i',[0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000])  #start with array empty 

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)  #extend by composition
    d = multiprocessing.Process(target=self.display, args=(self.pattern,))  #define process to run display() with the pattern as arument
    d.daemon = True   #start daemon process (terminates when main code ends)
    d.start() 

  def display(self, pattern): #display pattern continuously
    while True:
      for row in range(len(pattern)): #sequentially populate all rows
        self.shifter.shiftByte(~pattern[row]) #load the row values
        self.shifter.shiftByte(1 << (7 - row)) #select the given row
        self.shifter.ping(self.shifter.latchPin)  #ping the latch pin after sending 2 bytes
        sleep(0.001)
