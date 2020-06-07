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

from .dsp_ctrl_regs import CtrlDSP1_2, CtrlDSP3, CtrlDSP5__8
from .uart_ctrl_regs import CtrlUART1
from .stpm_ctrl_regs import CtrlDFE1_2
from .ev_regs import DataEVReg
from .dsp_data_regs import DataDSP1, DataDSP2__9, DataDSP14_15, DataDSP16_18, \
                          DataDSP17_19, DataChReg, Data32Reg

class CtrlRegs(object):
    def __init__(self):
        self._list = []
        self.dsp_ctrl_3 = CtrlDSP3(0x04, 0x000004E0)
        self._list.append(self.dsp_ctrl_3)
        self.dsp_ctrl_5 = CtrlDSP5__8(0x08, 0x003FF800)
        self._list.append(self.dsp_ctrl_5)
        self.dsp_ctrl_6 = CtrlDSP5__8(0x0A, 0x003FF800)
        self._list.append(self.dsp_ctrl_6)
        self.dsp_ctrl_7 = CtrlDSP5__8(0x0C, 0x003FF800)
        self._list.append(self.dsp_ctrl_7)
        self.dsp_ctrl_8 = CtrlDSP5__8(0x0E, 0x003FF800)
        self._list.append(self.dsp_ctrl_8)
        self.dfe_ctrl_1 = CtrlDFE1_2(0x18, 0x0F270327)
        self._list.append(self.dfe_ctrl_1)
        self.uart_ctrl_1 = CtrlUART1(0x24, 0x00004007)
        self._list.append(self.uart_ctrl_1)

    def len(self):
        return len(self._list)

    def list(self):
        return self._list

class DataRegs(object):
    def __init__(self):
        self._list = []
        self.dsp_reg14 = DataDSP14_15(0x48)
        self._list.append(self.dsp_reg14)
        self.dsp_reg15 = DataDSP14_15(0x4a)
        self._list.append(self.dsp_reg15)

    def len(self):
        return len(self._list)

    def list(self):
        return self._list
