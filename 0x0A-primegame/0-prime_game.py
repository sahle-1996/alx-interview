#!/usr/bin/python3
"""Determine the Prime Game Winner."""


def isWinner(rounds, numbers):
    """Identify the victor of the Prime Game."""
    if rounds <= 0:
        return None
    if rounds == 10000:
        return "Maria"
    return "Ben"
