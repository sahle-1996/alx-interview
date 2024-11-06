#!/usr/bin/python3
"""
Solves the N Queens puzzle where N non-attacking queens
are placed on an N×N chessboard.
"""
from sys import argv, exit


def place_n_queens(size):
    """Solves the N queens challenge and returns solutions"""
    solutions = []
    positions = [-1] * size
    # 'positions' represents the queen's column position per row

    def search(row):
        """Recursively searches for valid queen placements"""
        if row == len(positions):  # all queens are correctly placed
            solutions.append(positions[:])
            return
        for col in range(len(positions)):
            positions[row] = col
            if is_safe(row):  # ensures no attacks
                search(row + 1)

    def is_safe(current_row):
        """Checks if the queen at current_row is safe"""
        for prev_row in range(current_row):
            if positions[prev_row] == positions[current_row]:  # same column
                return False
            if abs(positions[prev_row] - positions[current_row]) == current_row - prev_row:  # same diagonal
                return False
        return True

    def format_solutions(solutions):
        """Formats solutions for display"""
        boards = []
        for solution in solutions:
            board = []
            for row, col in enumerate(solution):
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
        results = place_n_queens(size)
        for solution in results:
            print(solution)
