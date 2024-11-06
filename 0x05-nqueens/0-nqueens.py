#!/usr/bin/python3
"""
Module to solve the N Queens problem by placing N non-attacking queens
on an N×N chessboard.
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    size = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if size < 4:
    print("N must be at least 4")
    sys.exit(1)


def find_n_queens(n):
    """Finds all possible solutions for placing N queens."""
    columns = set()  # columns with queens
    positive_diag = set()  # r + c for positive diagonals
    negative_diag = set()  # r - c for negative diagonals

    solutions = []  # stores all solutions
    board_state = [[] for _ in range(n)]  # current board configuration

    def search(row):
        """Uses recursion and backtracking to find valid queen placements."""
        if row == n:  # all queens placed
            solutions.append(board_state[:])
            return

        for col in range(n):
            if col in columns or (row + col) in positive_diag or (row - col) in negative_diag:
                continue

            # Place queen and mark column and diagonals
            columns.add(col)
            positive_diag.add(row + col)
            negative_diag.add(row - col)
            board_state[row] = [row, col]

            search(row + 1)  # move to next row

            # Remove queen and unmark column and diagonals
            columns.remove(col)
            positive_diag.remove(row + col)
            negative_diag.remove(row - col)
            board_state[row] = []

    search(0)
    return solutions


if __name__ == "__main__":
    results = find_n_queens(size)
    for solution in results:
        print(solution)
