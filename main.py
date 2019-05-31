# CSP problem with use of back-tracking algorithm and forward checking heuristic

import board
import utils
import csp

size = 3
b = board.Board(size, utils.generate_visibilities(size))
b.print_board()
b.print_constraints()

csp.find_solution(-1, 0, 0, b)
