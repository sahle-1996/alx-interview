#!/usr/bin/python3
"""UTF-8 Encoding Validation"""


def count_leading_ones(byte):
    """Count leading 1-bits in a byte."""
    leading_ones = 0
    mask = 1 << 7
    while mask & byte:
        leading_ones += 1
        mask >>= 1
    return leading_ones


def is_valid_utf8(data):
    """Check if a list of bytes represents valid UTF-8 encoding."""
    remaining_bytes = 0
    for byte in data:
        if remaining_bytes == 0:
            leading_ones = count_leading_ones(byte)
            # Single-byte character (0xxxxxxx)
            if leading_ones == 0:
                continue
            # UTF-8 characters are between 1 and 4 bytes long
            if leading_ones == 1 or leading_ones > 4:
                return False
            remaining_bytes = leading_ones - 1
        else:
            # Continuation byte (10xxxxxx)
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
            remaining_bytes -= 1
    return remaining_bytes == 0
