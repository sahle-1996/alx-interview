#!/usr/bin/python3
"""UTF-8 Encoding Validation"""


def count_initial_ones(byte):
    """Counts leading 1-bits in an integer."""
    count = 0
    mask = 1 << 7
    while mask & byte:
        count += 1
        mask >>= 1
    return count


def validUTF8(data):
    """Checks if a list of integers is valid UTF-8 encoded data."""
    remaining_bytes = 0
    for byte in data:
        if remaining_bytes == 0:
            leading_ones = count_initial_ones(byte)
            # Single-byte character (0xxxxxxx)
            if leading_ones == 0:
                continue
            # UTF-8 encoding limits characters to 1 to 4 bytes
            if leading_ones == 1 or leading_ones > 4:
                return False
            remaining_bytes = leading_ones - 1
        else:
            # Continuation byte (10xxxxxx)
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
            remaining_bytes -= 1
    return remaining_bytes == 0
