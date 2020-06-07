Copyright (c) 2020 Tyler Cone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

from machine import Pin, SPI
from stpm34 import Stpm34
import time


class Smartlet:
    def __init__(self):
        self.spi = SPI(2, baudrate=200000, polarity=1, phase=1, bits=8, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
        self.meter1 = Stpm34(self.spi, Pin(12, Pin.OUT, Pin.PULL_UP, value=1))
        self.meter2 = Stpm34(self.spi, Pin(13, Pin.OUT, Pin.PULL_UP, value=1))

    def run(self):
        while True:
            print("Meter 1: (V1, C1, V2, C2)")
            print(self.meter1.read())
            print("Meter 2: (V1, C1, V2, C2)")
            print(self.meter2.read())
            time.sleep(1)
