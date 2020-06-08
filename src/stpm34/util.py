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


def bitwise_reverse(n):
    n = ((n >> 1) & 0x55) | ((n << 1) & 0xaa)
    n = ((n >> 2) & 0x33) | ((n << 2) & 0xcc)
    n = ((n >> 4) & 0x0F) | ((n << 4) & 0xF0)
    return n


def crc8(bytes_, sum_=0x00, poly_=0x07):
    if isinstance(bytes_, str):
        raise TypeError("Unicode-objects must be encoded before hashing")
    elif not isinstance(bytes_, (bytes, bytearray)):
        raise TypeError("object supporting the buffer API required")
    _sum = sum_
    _poly = poly_
    for byte in bytes_:
        _sum = __calc(byte, _sum, _poly)
    return _sum


def __calc(b, s, crc_8):
    for _ in range(8):
        t = b ^ s
        s <<= 1
        if t & 0x80:
            s ^= crc_8
        b <<= 1
        s &= 0xFF
    return s
