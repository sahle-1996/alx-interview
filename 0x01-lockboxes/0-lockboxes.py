#!/usr/bin/python3
"""
This module offers a function that checks if all the boxes
in a list of lists can be unlocked.
"""


def canUnlockAll(boxes):
    """
    This function takes a list of lists where each list represents
        a box and its available keys. It returns True if all boxes
        can be unlocked, otherwise False. The first box is open by default.

    Parameters:
    boxes (List[List[int]]): A list of boxes, each containing keys.

    Returns:
    bool: True if every box can be unlocked, otherwise False.
    """
    total_boxes = len(boxes)
    opened_boxes = {0}
    keys = set(boxes[0]) - {0}

    while keys:
        current_key = keys.pop()
        if current_key < total_boxes and current_key not in opened_boxes:
            keys.update(boxes[current_key])
            opened_boxes.add(current_key)

    return len(opened_boxes) == total_boxes
