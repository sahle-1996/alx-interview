#!/usr/bin/python3
"""Making change with minimal coins"""


def makeChange(coins, total):
    """Determine the fewest coins needed to meet a given total

    Args:
        coins (list): Values of coins available
        total (int): Target amount to reach

    Returns:
        int: Fewest number of coins, or -1 if not possible
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    remaining = total
    count = 0
    for coin in coins:
        if remaining <= 0:
            break
        used = remaining // coin
        count += used
        remaining -= used * coin
    return count if remaining == 0 else -1
