#!/usr/bin/env python3
'''A module for generating Pascal's triangle.
'''


def pascal_triangle(n):
    '''Returns a list of lists representing Pascal's triangle of size n.
    '''
    if not isinstance(n, int) or n <= 0:
        return []
    result = []
    for row in range(n):
        current = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current.append(1)
            else:
                current.append(result[row - 1][col - 1] + result[row - 1][col])
        result.append(current)
    return result
