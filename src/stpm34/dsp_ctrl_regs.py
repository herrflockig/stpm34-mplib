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


class CtrlDSP1_2(Register):
    """Control Register for DSP regs 1 and 2

    Documentation:
    ==============

    +---------+-----------------+------------------------------------------+---------+
    | Bit     | Internal signal | Description                              | Default |
    +---------+-----------------+------------------------------------------+---------+
    | [3:0]   | CLRSS_TO1       | Set duration of primary channel signal   | 0x0     |
    |         |                 | to clear sag and swell and avoid race    |         |
    |         |                 | condition on digital counters            |         |
    +---------+-----------------+------------------------------------------+---------+
    | 4       | ClearSS1        | Clear sag and swell time register and    | 0x0     |
    |         |                 | history bits for primary channel,        |         |
    |         |                 | auto-reset to '0'                        |         |
    +---------+-----------------+------------------------------------------+---------+
    | 5       | ENVREF1         | Enable internal voltage reference for    | 0x1     |
    |         |                 | primary channel:                         |         |
    |         |                 |     0: reference disabled – external     |         |
    |         |                 |        VREF required                     |         |
    |         |                 |     1: reference enabled                 |         |
    +---------+-----------------+------------------------------------------+---------+
    | [8:6]   | TC1             | Temperature compensation coefficient     | 0X2     |
    |         |                 | selection for primary channel voltage    |         |
    |         |                 | reference VREF1 (see Table 9)            |         |
    +---------+-----------------+------------------------------------------+---------+
    | [16:9]  |                 | Reserved                                 | 0x0     |
    +---------+-----------------+------------------------------------------+---------+
    | 17      | AEM1            | Apparent energy mode for primary         | 0x0     |
    |         |                 | channel:                                 |         |
    |         |                 |     0: use apparent RMS power            |         |
    |         |                 |     1: use apparent vectorial power      |         |
    +---------+-----------------+------------------------------------------+---------+
    | 18      | APM1            | Apparent vectorial power mode for        | 0x0     |
    |         |                 | primary channel:                         |         |
    |         |                 |     0: use fundamental power             |         |
    |         |                 |     1: use active power                  |         |
    +---------+-----------------+------------------------------------------+---------+
    | 19      | BHPFV1          | Bypass hi-pass filter for primary        | 0x0     |
    |         |                 | voltage channel:                         |         |
    |         |                 |     0: HPF enabled                       |         |
    |         |                 |     1: HPF bypassed                      |         |
    +---------+-----------------+------------------------------------------+---------+
    | 20      | BHPFC1          | Bypass hi-pass filter for primary        | 0x0     |
    |         |                 | current channel:                         |         |
    |         |                 |     0: HPF enabled                       |         |
    |         |                 |     1: HPF bypassed                      |         |
    +---------+-----------------+------------------------------------------+---------+
    | 21      | ROC1            | Add Rogowski integrator to primary       | 0x0     |
    |         |                 | current channel filtering pipeline:      |         |
    |         |                 |     0: integrator bypassed               |         |
    |         |                 |     1: integrator enabled                |         |
    +---------+-----------------+------------------------------------------+---------+
    | [23:22] |                 | Reserved                                 | 0x0     |
    +---------+-----------------+------------------------------------------+---------+
    | [27:24] | LPW1            | LED1 speed dividing factor:              | 0x4     |
    |         |                 |     0x0 = 2^(-4), 0xF = 2^11             |         |
    |         |                 | Default 0x4 = 1                          |         |
    +---------+-----------------+------------------------------------------+---------+
    | [29:28] | LPS1            | LED1 pulse-out power selection:          | 0x0     |
    |         |                 | LPS1 [1:0]: 00,01,10,11                  |         |
    |         |                 | LED1 output: active, fundamental,        |         |
    |         |                 |              reactive, apparent          |         |
    +---------+-----------------+------------------------------------------+---------+
    | [31:30] | LCS1            | LED1 pulse-out channel selection:        |  0x0    |
    |         |                 | LCS1 [1:0]: 00,01,10,11                  |         |
    |         |                 | LED1: primary channels, secondary        |         |
    |         |                 |       channels, cumulative,              |         |
    |         |                 |       sigma-delta bitstream              |         |
    +---------+-----------------+------------------------------------------+---------+
    """
    def __init__(self, address, value):
        fields = {
            "clear_sag_swell_timeout": Field(0, 4),
            "clear_sag_swell": Field(4),
            "en_vref": Field(5),
            "temp_comp": Field(6, 3),
            "apparent_energy_mode": Field(17),
            "apparent_vec_pow_mode": Field(18),
            "bypass_HPF_volt": Field(19),
            "bypass_HPF_current": Field(20),
            "ROC_bypass": Field(21),
            "LED_speed_drv": Field(24, 4),
            "LED_pow_sel": Field(28, 2),
            "LED_channel_sel": Field(30, 2)
        }
        super(CtrlDSP1_2, self).__init__(address, value, fields)


class CtrlDSP3(Register):
    def __init__(self, address=0x04, value=0x000004E0):
        fields = {
            "clk_out_sel": Field(14, 2),
            "clk_out_en": Field(16),
            "tamper_tolerance": Field(17, 2),
            "tamper_en": Field(19),
            "software_reset": Field(20),
            "software_latch1": Field(21),
            "software_latch2": Field(22),
            "software_auto_latch": Field(23),
            "LED1_off": Field(24),
            "LED2_off": Field(25),
            "diff_energy_calc_en": Field(26),
            "ref_freq": Field(27)
        }
        super(CtrlDSP3, self).__init__(address, value, fields)


class CtrlDSP4(Register):
    def __init__(self, address=0x06, value=0x00000000):
        fields = {
            "secondary_current_phase_comp": Field(0, 10),
            "secondary_voltage_phase_comp": Field(10, 2),
            "primary_current_phase_comp": Field(12, 10),
            "primary_voltage_phase_comp": Field(22, 2)
        }
        super(CtrlDSP4, self).__init__(address, value, fields)


class CtrlDSP5__8(Register):
    def __init__(self, address, value=0x003FF800):
        fields = {
            "calibration": Field(0, 12),
            "swell_thresh": Field(12, 10),
            "sag_thresh": Field(22, 10)
        }
        super(CtrlDSP5__8, self).__init__(address, value, fields)


class CtrlDSP9_11(Register):
    def __init__(self, address, value=0x00000FFF):
        fields = {
            "ah_rms_upper_thresh": Field(0, 12),
            "active_pow_offset": Field(12, 10),
            "fundamental_pow_offset": Field(22, 10)
        }
        super(CtrlDSP9_11, self).__init__(address, value, fields)


class CtrlDSP10_12(Register):
    def __init__(self, address, value=0x00000FFF):
        fields = {
            "ah_rms_lower_thresh": Field(0, 12),
            "reactive_pow_offset": Field(12, 10),
            "apparent_pow_offset": Field(22, 10)
        }
        super(CtrlDSP10_12, self).__init__(address, value, fields)
