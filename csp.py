import board
import utils


def find_solution_bt(index, row, col, b):
    n = board.get_n()
    vals = [i for i in range(1, n+1)]

    if index < 0:
        index += 1
        b.board[row][col] = vals[index]

    if row == n-1 and col == n-1 and b.check_constraint_column(col, b.constraints()) and b.check_constraint_row(row, b.constraints()) and b.is_latin_square_valid():
        b.correct = True
        return b

    if not b.is_valid_latin_square(row, col) or not b.check_constraint_column(col, b.constraints()) or not b.check_constraint_row(row, b.constraints()):
        if index == n-1:
            find_solution_bt(-1, row, col, b)
        index += 1
        b.board[row][col] = vals[index]

    return board