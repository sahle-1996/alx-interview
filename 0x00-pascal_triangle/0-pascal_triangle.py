#!/usr/bin/python3
'''A module for working with Pascal's triangle.'''

def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.'''
    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle

    for row_num in range(n):
        row = []
        for col_num in range(row_num + 1):
            if col_num == 0 or col_num == row_num:
                row.append(1)
            else:
                row.append(triangle[row_num - 1][col_num - 1] + triangle[row_num - 1][col_num])
        triangle.append(row)

    return triangle
