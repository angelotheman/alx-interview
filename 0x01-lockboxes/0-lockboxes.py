#!/usr/bin/python3
"""
Solve the mock interview
"""


def canUnlockAll(boxes):
    """
    Unlock the boxes
    """
    if not boxes:
        return False

    n = len(boxes)
    opened = set()
    opened.add(0)
    keys = list(boxes[0])

    while keys:
        key = keys.pop(0)

        if key < n and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == n
