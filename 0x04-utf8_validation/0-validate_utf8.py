#!/usr/bin/python3
"""
Function UTF-8 Validation
"""


def validUTF8(data):
    """Defining UTF8"""
    bits_count = 0

    for byte in data:
        if bits_count == 0:
            if (byte >> 5) == 0b110:
                bits_count = 1
            elif (byte >> 4) == 0b1110:
                bits_count = 2
            elif (byte >> 3) == 0b11110:
                bits_count = 3
            elif (byte >> 7) != 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            bits_count -= 1
    return bits_count == 0
