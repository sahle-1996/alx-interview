#!/usr/bin/env python3
"""Coin change problem solver"""


def makeChange(coins, total):
    """Calculate the minimum coins needed for a given total.

    Args:
        coins (list): List of available coin denominations.
        total (int): The amount to achieve using the coins.

    Returns:
        int: Minimum number of coins needed or -1 if not possible.
    """
    if total <= 0:
        return 0
    current_sum = 0
    coin_count = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        while current_sum + coin <= total:
            current_sum += coin
            coin_count += 1
        if current_sum == total:
            return coin_count
    return -1
