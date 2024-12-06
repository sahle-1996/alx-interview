#!/usr/bin/python3
"""
0. Island perimeter
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island without lakes."""
    if not isinstance(grid, list):
        return 0
    perimeter = 0
    rows = len(grid)
    for r, line in enumerate(grid):
        cols = len(line)
        for c, val in enumerate(line):
            if val == 0:
                continue
            edges = (
                r == 0 or (len(grid[r - 1]) > c and grid[r - 1][c] == 0),
                c == cols - 1 or (cols > c + 1 and line[c + 1] == 0),
                r == rows - 1 or (len(grid[r + 1]) > c and grid[r + 1][c] == 0),
                c == 0 or line[c - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
