#!/usr/bin/python3
"""
Module for N-Queens Problem Solution.
For solving and printing possible board arrangements.
"""
from sys import argv, exit


def n_queens_solution(size):
    """Generates solutions to the N-Queens puzzle"""
    solutions = []
    positions = [-1] * size
    # 'positions' is a 1D array where index is row and value is column.

    def search(row):
        """Recursive function for solving N-Queens using backtracking"""
        if row == len(positions):  # all queens are placed correctly
            solutions.append(positions[:])
            return
        for col in range(len(positions)):
            positions[row] = col
            if is_safe(row):  # checks safety of queen's position
                search(row + 1)

    def is_safe(current_row):
        """Verifies no queens are attacking each other"""
        for prev_row in range(current_row):
            if positions[prev_row] == positions[current_row]:  # same column
                return False
            if abs(positions[prev_row] - positions[current_row]) == current_row - prev_row:  # same diagonal
                return False
        return True

    def format_solutions(solutions):
        """Formats the solution into a list of board positions"""
        boards = []
        for queens in solutions:
            board = []
            for row, col in enumerate(queens):
                board.append([row, col])
            boards.append(board)
        return boards

    search(0)
    return format_solutions(solutions)


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        size = int(argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if size < 4:
        print('N must be at least 4')
        exit(1)
    else:
        results = n_queens_solution(size)
        for solution in results:
            print(solution)
