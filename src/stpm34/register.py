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

from .field import Field

class Register(object):
    def __init__(self, address, value=0, fields=None):
        self.address = address
        self._valid_fields = True
        if fields is not None and isinstance(fields, dict):
            for field in fields.values():
                if not isinstance(field, Field):
                    self._valid_fields = False
                    print("Field dict contains non-Field")
            if self._valid_fields:
                self.fields = fields
                self.from_uint32(value)
        else:
            self._valid_fields = False
            self.fields = {}

    def from_uint32(self, value):
        for field in self.fields.values():
            field.offset_val = value

    def to_uint32(self):
        result = 0
        for field in self.fields.values():
            result |= field.offset_val
        return result

    def to_bytes(self):
        i = self.to_uint32()
        b = bytearray(4)
        b[0] = (i >> 0) & 0xFF
        b[1] = (i >> 8) & 0xFF
        b[2] = (i >> 16) & 0xFF
        b[3] = (i >> 24) & 0xFF
        return bytes(b)
