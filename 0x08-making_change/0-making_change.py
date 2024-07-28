#!/usr/bin/env python3
"""
Working with dynamic
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total amount.

    Args:
        coins (list): A list of coin values.
        total (int): The total amount to reach.

    Returns:
        int: The fewest number of coins needed, or -1 if impossible.
    """
    if total <= 0:
        return 0

    # Create a table to store the fewest number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to reach 0 amount

    # Fill up the table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the total amount cannot be reached, return -1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
