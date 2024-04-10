#!/usr/bin/python3
"""
 Queen, Backtracking
"""

import sys


def solve_nqueens(n):
    """Solves the N queens problem recursively."""
    if n == 0:
        return [[]]
    inner_solution = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(n_q)
            for solution in inner_solution
            if safe_queen((n, i + 1), solution)]


def attack_queen(square, queen):
    """Checks an attack between two queens."""
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def safe_queen(sqr, queens):
    """Checks queen placement."""
    for queen in queens:
        if attack_queen(sqr, queen):
            return False
    return True
