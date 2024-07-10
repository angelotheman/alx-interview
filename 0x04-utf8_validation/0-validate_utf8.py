#!/usr/bin/python
"""
UTF-Validation
"""


def validUTF8(data):
    """
    Number of bytes in the current UTF-8 character
    """
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's in the first byte
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            # If num_bytes is 0, then it's a 1-byte character (ASCII)
            if num_bytes == 0:
                continue

            # If num_bytes is more than 4 or 1, it's not a valid UTF-8 encoding
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If the current byte doesn't start with '10', it's not valid
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes to process
        num_bytes -= 1

    # If we finished processing all bytes, num_bytes should be 0
    return num_bytes == 0
