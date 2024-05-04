#!/usr/bin/python3
"""Making change module."""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins required to reach
    a given total amount using different coin denominations.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin value
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return dp[total] if < float('inf') (total can be formed), else -1
    return dp[total] if dp[total] != float('inf') else -1
