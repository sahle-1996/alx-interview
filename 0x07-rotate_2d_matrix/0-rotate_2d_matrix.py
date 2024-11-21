#!/usr/bin/python3
""" Rotate a 2D Matrix by 90 degrees clockwise
"""


def rotate_matrix_90_degrees(mat):
    """ Rotate an n x n matrix 90 degrees in a clockwise direction
    """
    for i, row in enumerate(zip(*mat[::-1])):
        mat[i] = list(row)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    rotate_matrix_90_degrees(matrix)
    print(matrix)
