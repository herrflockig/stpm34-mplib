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

from .register import Register
from .field import Field


class CtrlUART1(Register):
    def __init__(self, address=0x24, value=0x00004007):
        fields = {
            "crc_poly": Field(0, 8),
            "noise_cancel_en": Field(8),
            "break_on_err": Field(9),
            "crc_en": Field(14),
            "lsb_first": Field(15),
            "timeout": Field(16, 8)
        }
        super(CtrlUART1, self).__init__(address, value, fields)


class CtrlUART2(Register):
    def __init__(self, address=0x26, value=0x00000683):
        fields = {
            "baud": Field(0, 16),
            "frame_delay": Field(16, 8)
        }
        super(CtrlUART2, self).__init__(address, value, fields)


class CtrlUARTStatus(Register):
    def __init__(self, address=0x28, value=0x00000000):
        fields = {
            "irq_uart_crc_error": Field(1),
            "irq_time_out_err": Field(2),
            "irq_frame_err": Field(3),
            "irq_noise_err": Field(4),
            "irq_rx_ovr": Field(5),
            "irq_tx_ovr": Field(6),
            "irq_rx_full": Field(8),
            "irq_tx_empty": Field(9),
            "irq_read_error": Field(10),
            "irq_write_error": Field(11),
            "irq_spi_crc_error": Field(12),
            "irq_underrun": Field(13),
            "irq_overrun": Field(14),
            "break_received": Field(16),
            "uart_crc_error": Field(17),
            "time_out_err": Field(18),
            "frame_err": Field(19),
            "noise_err": Field(20),
            "rx_ovr": Field(21),
            "tx_ovr": Field(22),
            "rx_full": Field(24),
            "tx_empty": Field(25),
            "read_error": Field(26),
            "write_error": Field(27),
            "spi_crc_error": Field(28),
            "underrun": Field(29),
            "overrun": Field(30)
        }
        super(CtrlUARTStatus, self).__init__(address, value, fields)
