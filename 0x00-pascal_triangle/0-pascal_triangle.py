#!/usr/bin/python3
'''An alternative module for generating Pascal's triangle.'''

def pascal_triangle(n):
    '''Generates Pascal's triangle as a list of lists for a given integer n.'''
    if not isinstance(n, int) or n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row
    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1]  # Start each row with 1
        curr_row.extend(prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1))
        curr_row.append(1)  # End each row with 1
        triangle.append(curr_row)
    
    return triangle
