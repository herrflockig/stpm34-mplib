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


class DataEVReg(Register):
    def __init__(self, address):
        fields = {
            "ev_sign_tot_pow_a": Field(0),  # Sign of total active power
            "ev_sign_tot_pow_r": Field(1),  # Sign of total reactive power
            "ev_ovf_tot_pow_a": Field(2),  # total active power triggered threshold
            "ev_ovf_tot_pow_r": Field(3),  # total reactive power triggered threshold
            "ev_pow_sign_a": Field(4),  # Sign of channel active power
            "ev_pow_sign_f": Field(5),  # Sign of channel fundamental power
            "ev_pow_sign_r": Field(6),  # Sign of channel reactive power
            "ev_pow_sign_s": Field(7),  # Sign of channel apparent power
            "ev_energy_ovf_a": Field(8),  # channel active power triggered threshold
            "ev_energy_ovf_f": Field(9),  # channel fundamental power triggered threshold
            "ev_energy_ovf_r": Field(10),  # channel reactive power triggered threshold
            "ev_energy_ovf_s": Field(11),  # channel apparent power triggered threshold
            "ev_cur_zero_cross": Field(12),  # channel current crossed zero
            "ev_cur_ADC_stuck": Field(13),  # channel current ADC stuck...
            "ev_cur_AH_accum": Field(14),  # channel Amp Hour accumulation event occured
            "ev_cur_swell_hist": Field(15, 4),  # channel current swell event history
            "ev_volt_zero_cross": Field(19),  # channel voltage crossed zero
            "ev_volt_ADC_stuck": Field(20),  # channel voltage ADC stuck...
            "ev_volt_period_err": Field(21),  # channel voltage period error (out of range
            "ev_volt_swell_hist": Field(22, 4),  # channel voltage swell event history
            "ev_volt_sag_hist": Field(26, 4)  # channel voltage sag event history
        }
        super(DataEVReg, self).__init__(address, 0, fields)
