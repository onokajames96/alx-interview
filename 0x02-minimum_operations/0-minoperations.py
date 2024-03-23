#!/usr/bin/python3
"""
Algorithm and Python
"""


def minOperations(n):
    """
    Returns an integer
    If n is impossible to achieve, return 0
    """
    num_ope = 0
    min_ope = 2
    while n > 1:
        while n % min_ope == 0:
            num_ope += min_ope
            n /= min_ope
        min_ope += 1
    return num_ope
