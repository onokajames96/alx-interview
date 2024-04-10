#!/usr/bin/python3
"""The N Queens challenge"""

import sys


def is_n_queen(cell: list) -> bool:
    """Check if a queen can be placed at a given position."""
    row_number = len(cell) - 1
    for i in range(row_number):
        col_diff = abs(cell[i] - cell[row_number])
        if col_diff == 0 or col_diff == row_number - i:
            return False
    return True


def solve_n_queens(dimension: int, row: int, cell: list, result: list):
    """Recursively solve the N queens problem."""
    if row == dimension:
        print(result)
    else:
        for column in range(dimension):
            cell.append(column)
            result.append([row, column])
            if is_n_queen(cell):
                solve_n_queens(dimension, row + 1, cell, result)
            cell.pop()
            result.pop()


if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if n < 4:
    print('N must be at least 4')
    sys.exit(1)
else:
    result = []
    solve_n_queens(n, 0, [], result)
