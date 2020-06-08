"""
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
"""

from .register import Register
from .field import Field


class DataDSP1(Register):
    def __init__(self, address=0x2E):
        fields = {
            "ch1_period": Field(0, 12),
            "ch2_period": Field(16, 12)
        }
        super(DataDSP1, self).__init__(address, 0, fields)


class DataDSP2__9(Register):
    def __init__(self, address):
        fields = {
            "data": Field(0, 24)
        }
        super(DataDSP2__9, self).__init__(address, 0, fields)


class DataDSP14_15(Register):
    def __init__(self, address):
        fields = {
            "vrms": Field(0, 15), "crms": Field(15, 17)
        }
        super(DataDSP14_15, self).__init__(address, 0, fields)


class DataDSP16_18(Register):
    def __init__(self, address):
        fields = {
            "swell_time": Field(0, 15),
            "sag_time": Field(16, 15)
        }
        super(DataDSP16_18, self).__init__(address, 0, fields)


class DataDSP17_19(Register):
    def __init__(self, address):
        fields = {
            "swell_time": Field(0, 15),
            "phase_angle": Field(16, 12)
        }
        super(DataDSP17_19, self).__init__(address, 0, fields)


class DataChReg(Register):
    def __init__(self, address):
        fields = {
            "data": Field(0, 29)
        }
        super(DataChReg, self).__init__(address, 0, fields)


class Data32Reg(Register):
    def __init__(self, address):
        fields = {
            "data": Field(0, 32)
        }
        super(Data32Reg, self).__init__(address, 0, fields)
