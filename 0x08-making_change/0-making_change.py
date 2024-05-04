#!/usr/bin/python3
"""Making change module."""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to make up the given total value
    using the available coin denominations. If it's impossible to make the
    total,
    return -1.
    """
    if total <= 0:
        return 0

    # Create a list to store the minimum number of coins for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin value
    for coin in coins:
        # Update dp array for each amount from coin value to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return dp[total] if < float('inf') (total can be formed), else -1
    return dp[total] if dp[total] != float('inf') else -1
