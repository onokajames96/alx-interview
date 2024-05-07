#!/usr/bin/python3
""" Function for geting island perimeter grid"""


def island_perimeter(grid):
    """Calculate the perimeter of the island described in grid."""

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                neighbors = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
                for (nr, nc) in neighbors:
                    if (nr < 0 or nr >= rows or nc < 0 or nc >= cols or
                            grid[nr][nc] == 0):
                        perimeter += 1

    return perimeter
