#!/usr/bin/python3
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

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Create a table to store the fewest number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to reach 0 amount

    # Fill up the table
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
            else:
                break  # No need to check smaller coins

    # If the total amount cannot be reached, return -1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
