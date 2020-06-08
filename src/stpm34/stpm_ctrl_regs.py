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


class CtrlDFE1_2(Register):
    def __init__(self, address, value):
        fields = {
            "volt_reading_en": Field(0),
            "current_reading_en": Field(16),
            "gain": Field(26, 2)
        }
        super(CtrlDFE1_2, self).__init__(address, value, fields)


class CtrlIRQ(Register):
    def __init__(self, address, value=0x00000000):
        fields = {
            "tot_sign_pow_a": Field(0),
            "tot_sign_pow_r": Field(1),
            "tot_energy_ovf_a": Field(2),
            "tot_energy_ovf_r": Field(3),
            "ch2_sign_pow_a": Field(4),
            "ch2_sign_pow_f": Field(5),
            "ch2_sign_pow_r": Field(6),
            "ch2_sign_pow_s": Field(7),
            "ch2_energy_ovf_a": Field(8),
            "ch2_energy_ovf_f": Field(9),
            "ch2_energy_ovf_r": Field(10),
            "ch2_energy_ovf_s": Field(11),
            "ch1_sign_pow_a": Field(12),
            "ch1_sign_pow_f": Field(13),
            "ch1_sign_pow_r": Field(14),
            "ch1_sign_pow_s": Field(15),
            "ch1_energy_ovf_a": Field(16),
            "ch1_energy_ovf_f": Field(17),
            "ch1_energy_ovf_r": Field(18),
            "ch1_energy_ovf_s": Field(19),
            "current_adc_stuck": Field(20),
            "ah_accum": Field(21),
            "current_swell_detect": Field(22),
            "current_swell_end": Field(23),
            "volt_adc_stuck": Field(24),
            "volt_period_err": Field(25),
            "volt_sag_detect": Field(26),
            "volt_sag_end": Field(27),
            "volt_swell_detect": Field(28),
            "volt_swell_end": Field(29),
            "tamper_on": Field(30),
            "tamper_or_wrong_conn": Field(31)
        }
        super(CtrlIRQ, self).__init__(address, value, fields)


class CtrlStatus(Register):
    def __init__(self, address, value=0x00000000):
        fields = {
            "tot_sign_pow_a": Field(0),
            "tot_sign_pow_r": Field(1),
            "tot_energy_ovf_a": Field(2),
            "tot_energy_ovf_r": Field(3),
            "ch2_sign_pow_a": Field(4),
            "ch2_sign_pow_f": Field(5),
            "ch2_sign_pow_r": Field(6),
            "ch2_sign_pow_s": Field(7),
            "ch2_energy_ovf_a": Field(8),
            "ch2_energy_ovf_f": Field(9),
            "ch2_energy_ovf_r": Field(10),
            "ch2_energy_ovf_s": Field(11),
            "ch1_sign_pow_a": Field(12),
            "ch1_sign_pow_f": Field(13),
            "ch1_sign_pow_r": Field(14),
            "ch1_sign_pow_s": Field(15),
            "ch1_energy_ovf_a": Field(16),
            "ch1_energy_ovf_f": Field(17),
            "ch1_energy_ovf_r": Field(18),
            "ch1_energy_ovf_s": Field(19),
            "current_adc_stuck": Field(20),
            "ah_accum": Field(21),
            "current_swell_detect": Field(22),
            "current_swell_end": Field(23),
            "volt_adc_stuck": Field(24),
            "volt_period_err": Field(25),
            "volt_sag_detect": Field(26),
            "volt_sag_end": Field(27),
            "volt_swell_detect": Field(28),
            "volt_swell_end": Field(29),
            "tamper_on": Field(30),
            "tamper_or_wrong_conn": Field(31)
        }
        super(CtrlStatus, self).__init__(address, value, fields)
