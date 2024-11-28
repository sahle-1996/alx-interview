#!/usr/bin/env python3
"""Change Maker Module"""


def makeChange(coins, total):
    """Calculate the minimum coins to meet a total.

    Args:
        coins (list): Available denominations of coins.
        total (int): The total amount to make change for.

    Returns:
        int: Minimum number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0
    remaining = total
    count = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        while remaining >= coin:
            remaining -= coin
            count += 1
        if remaining == 0:
            return count
    return -1
