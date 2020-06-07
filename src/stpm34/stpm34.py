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

from .util import bitwise_reverse, crc8
from .register import Register
from .regs import CtrlRegs, DataRegs
import time


class Stpm34(object):
    """Class to control, read and configure an STPM34 module

    Parameters
    ----------
    uart : machine.UART
        The uart on which the device is communicating.

    Attributes
    ----------
    ctrl_regs : :obj:`stpm34.CtrlRegs`
        An object containing all of the control and configuration
        `stpm34.Register`'s of the device that you have specified. These get
        overwritten when you call `Stpm34.read_configs()`. They are written to
        the device when you call `Stpm34.apply_configs()`. You can also read or
        write Registers individually by calling `Stpm34.read_register(reg)` and
        `Stpm34.write_register(reg)` respectively.
    data_regs : :obj:`stpm34.DataRegs`
        An object containing all of the data `stpm34.Register`'s. This object
        is filled when you call `Stpm34.read()`. You should not write any of
        these Registers.

    Examples
    --------

    uart = UART(0, 9600) # STPM34 defaults to 9600 baud
    stpm = stpm34.Stpm34(uart)
    """

    # Pre defined parameters to the hardware
    Vref=1.18
    R1=998000.0
    R2=499.0
    ks=0.03115264797
    kint=1.0
    AV=2.0
    AI=2.0

    def __init__(self, bus, cs):
        self.bus = bus
        self.cs = cs

        self.ctrl_regs = CtrlRegs()
        self.data_regs = DataRegs()
        self._read_ctrl_regs = CtrlRegs()

        print("Before changing registers")
        self.read_configs()
        self.ctrl_regs.dsp_ctrl_3.fields["ref_freq"].val = 1
        self.write_register(self.ctrl_regs.dsp_ctrl_3)
        self.ctrl_regs.dfe_ctrl_1.fields["gain"].val = 0
        self.write_register(self.ctrl_regs.dfe_ctrl_1)
        print("After changing registers")
        self.apply_configs()
        #if not self.read_calibration():
        #    self.do_calibration()


    def latch(self, ch1=True, ch2=True):
        """Latches a measurement so that the registers can be read in from the device

        Parameters
        ----------
        ch1 : bool
            Set channel 1 latch, Default: True
        ch2 : bool
            Set channel 2 latch, Default: True
        """
        dsp3 = self.ctrl_regs.dsp_ctrl_3
        if ch1:
            dsp3.fields["software_latch1"].val = 1
        if ch2:
            dsp3.fields["software_latch2"].val = 1
        self.write_register(dsp3)
        ch1_latched = False
        ch2_latched = False
        latched = False
        dsp3 = self._read_ctrl_regs.dsp_ctrl_3
        countdown = 300
        while (not latched) and (countdown > 0):
            self.read_register(dsp3)
            if ch1 and dsp3.fields["software_latch1"].val == 0:
                ch1_latched = True
            if ch2 and dsp3.fields["software_latch2"].val == 0:
                ch2_latched = True
            latched = (not ch1 or ch1_latched) and (not ch2 or ch2_latched)
            if latched:
                break
            time.sleep_ms(1)
            countdown -= 1

    def read(self):
        self.latch()

        ch1_v, ch1_c = self.read_ch1_rms()
        ch2_v, ch2_c = self.read_ch2_rms()

        return ch1_v, ch1_c, ch2_v, ch2_c

    def do_calibration(self, nom_voltage=120.0, nom_current=0.25):
        print(nom_voltage, nom_current)
        n_samples = 200

        CALV1 = self.ctrl_regs.dsp_ctrl_5.fields["calibration"].val
        CALI1 = self.ctrl_regs.dsp_ctrl_6.fields["calibration"].val
        calv1 = (0.125 * (CALV1/2048)) + 0.75
        cali1 = (0.125 * (CALI1/2048)) + 0.75
        Xv = nom_voltage * self.AV * calv1 * (2**15) / (self.Vref * (1 + (self.R1/self.R2)))
        Xi = nom_current * self.AI * cali1 * self.ks * (2**17) / self.Vref

        v2_sum = 0
        c1_sum = 0
        for _ in range(n_samples):
            ch1_reg = self.read_register(self.data_regs.dsp_reg14)
            ch1_current = ch1_reg.fields["crms"].val
            c1_sum += ch1_current

            ch2_reg = self.read_register(self.data_regs.dsp_reg15)
            ch2_voltage = ch2_reg.fields["vrms"].val
            v2_sum += ch2_voltage

        Av = v2_sum / n_samples
        Ai = c1_sum / n_samples

        CALV = (14336.0 * (Xv/Av)) - 12288.0
        CALI = (14336.0 * (Xi/Ai)) - 12288.0

        self.write_calibration(int(CALV), int(CALI), int(CALV), int(CALI))

    def read_ch1_rms(self):
        # Channel 1
        CALV = self.ctrl_regs.dsp_ctrl_5.fields["calibration"].val
        CALI = self.ctrl_regs.dsp_ctrl_6.fields["calibration"].val
        reg = self.data_regs.dsp_reg14
        self.read_register(reg)

        calv = (0.125 * (CALV/2048.0)) + 0.75
        cali = (0.125 * (CALI/2048.0)) + 0.75
        v_reg = reg.fields["vrms"].val
        c_reg = reg.fields["crms"].val

        # using Vref,R1,R2,ks,calv,Av calculate voltage
        voltage = (v_reg * self.Vref * (1+(self.R1/self.R2))) / (calv * self.AV * (2**15))
        current = (c_reg * self.Vref) / (cali * self.AI * (2**17) * self.ks * self.kint)

        return voltage, current

    def read_ch2_rms(self):
        # Channel 2
        CALV = self.ctrl_regs.dsp_ctrl_7.fields["calibration"].val
        CALI = self.ctrl_regs.dsp_ctrl_8.fields["calibration"].val
        reg = self.data_regs.dsp_reg15
        self.read_register(reg)

        calv = (0.125 * (CALV/2048.0)) + 0.75
        cali = (0.125 * (CALI/2048.0)) + 0.75
        v_reg = reg.fields["vrms"].val
        c_reg = reg.fields["crms"].val

        # using Vref,R1,R2,ks,calv,Av calculate voltage
        voltage = (v_reg * self.Vref * (1+(self.R1/self.R2))) / (calv * self.AV * (2**15))
        current = (c_reg * self.Vref) / (cali * self.AI * (2**17) * self.ks * self.kint)

        return voltage, current

    def read_calibration(self):
        try:
            with open("cal.txt", 'r') as f:
                CHV1 = int(f.readline()[:-1])
                CHC1 = int(f.readline()[:-1])
                CHV2 = int(f.readline()[:-1])
                CHC2 = int(f.readline()[:-1])

                self.ctrl_regs.dsp_ctrl_5.fields["calibration"].val = CHV1
                self.ctrl_regs.dsp_ctrl_6.fields["calibration"].val = CHC1
                self.ctrl_regs.dsp_ctrl_7.fields["calibration"].val = CHV2
                self.ctrl_regs.dsp_ctrl_8.fields["calibration"].val = CHC2

                self.write_register(self.ctrl_regs.dsp_ctrl_5)
                self.write_register(self.ctrl_regs.dsp_ctrl_6)
                self.write_register(self.ctrl_regs.dsp_ctrl_7)
                self.write_register(self.ctrl_regs.dsp_ctrl_8)
        except OSError:
            print("no calibration file, try if you must...")
            return False
        return True

    def write_calibration(self, CHV1, CHC1, CHV2, CHC2):
        self.ctrl_regs.dsp_ctrl_5.fields["calibration"].val = CHV1
        self.ctrl_regs.dsp_ctrl_6.fields["calibration"].val = CHC1
        self.ctrl_regs.dsp_ctrl_7.fields["calibration"].val = CHV2
        self.ctrl_regs.dsp_ctrl_8.fields["calibration"].val = CHC2

        self.write_register(self.ctrl_regs.dsp_ctrl_5)
        self.write_register(self.ctrl_regs.dsp_ctrl_6)
        self.write_register(self.ctrl_regs.dsp_ctrl_7)
        self.write_register(self.ctrl_regs.dsp_ctrl_8)

        with open("cal.txt", 'w') as f:
            f.write(str(CHV1) + '\n')
            f.write(str(CHC1) + '\n')
            f.write(str(CHV2) + '\n')
            f.write(str(CHC2) + '\n')

    def read_configs(self):
        """Reads the configs from the device into Ctrl Regs"""
        for reg in self._read_ctrl_regs.list():
            self.read_register(reg)
            print("Read reg 0x{:02X}: 0x{:08X}".format(reg.address, reg.to_uint32()))
        self.ctrl_regs = self._read_ctrl_regs
        return self.ctrl_regs

    def apply_configs(self):
        """Apply Ctrl Regs to the device"""
        for reg in self.ctrl_regs.list():
            self.write_register(reg)
        return self.read_configs()

    def read_register(self, reg):
        """Read an individual Register

        Parameters
        ----------
        reg : :obj:`stpm34.Register`
            The Register to read
        """
        if not isinstance(reg, Register):
            print("Not a register I can read...")
            return 0
        fwd_packet = self._write_read_device(reg.address, 0xFF, 0xFF, 0xFF)
        if not fwd_packet:
            print("No packet was read!")
            return 0
        crc = self._check_crc_en()
        if crc:
            self._check_crc(fwd_packet)
        if len(fwd_packet) != (5 if crc else 4):
            print("oopsie error (wrong size) got {} needed {}".format(len(fwd_packet), (5 if crc else 4)))
        reg.from_uint32(int.from_bytes(fwd_packet[:3], 'little'))
        return reg

    def write_register(self, reg):
        """Write an indivfwd_packetidual Register

        Parameters
        ----------
        reg : :obj:`stpm34.Register`
            The Register to write
        """
        if not isinstance(reg, Register):
            print("Not a register that I can write...")
            return
        reg_bytes = reg.to_bytes()
        self._write_read_device(reg.address, reg.address+1, reg_bytes[2], reg_bytes[3])
        self._write_read_device(reg.address, reg.address, reg_bytes[0], reg_bytes[1])

    def _check_crc_en(self):
        if self.ctrl_regs.uart_ctrl_1.fields["crc_en"].val == 1:
            if self._read_ctrl_regs.uart_ctrl_1.fields["crc_en"].val == 0:
                print("Read crc disabled device side, but you're the boss.")
        if self.ctrl_regs.uart_ctrl_1.fields["crc_en"].val == 0:
            if self._read_ctrl_regs.uart_ctrl_1.fields["crc_en"].val == 1:
                print("Read crc enabled device side, but you're the boss.")
        return self.ctrl_regs.uart_ctrl_1.fields["crc_en"].val == 1

    def _write_read_device(self, read_address, write_address, lsbyte, msbyte):
        fwd_packet = bytes([read_address, write_address, lsbyte, msbyte])
        if self._check_crc_en():
            fwd_packet += bytes([crc8(fwd_packet)])
        self.cs.value(1)
        self.cs.value(0)
        self.bus.write(fwd_packet)
        self.cs.value(1)
        self.cs.value(0)
        if self._check_crc_en():
            ret = self.bus.read(5, 0xff)
        else:
            ret = self.bus.read(4, 0xff)
        self.cs.value(1)
        return ret

    def _check_crc(self, packet):
        if packet and len(packet) == 5:
            hash = crc8(packet[:4])
            if hash != packet[4]:
                print("crc error calc'd 0x{:02X} recv'd 0x{:02X}".format(hash, packet[4]))
        else:
            print("crc error (wrong size) got {} needed 5".format(len(packet)))
