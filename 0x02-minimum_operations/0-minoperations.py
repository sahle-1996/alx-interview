#!/usr/bin/python3
""" Minimum Operations
"""

def minOperations(n: int) -> int:
    """ Calculate the minimum number of operations required
    to achieve exactly n H characters.
    """
    current = 'H'
    clipboard = 'H'
    operations = 0
    while len(current) < n:
        if n % len(current) == 0:
            operations += 2
            clipboard = current
            current += current
        else:
            operations += 1
            current += clipboard
    return operations if len(current) == n else 0
