import math


class Board:
    def __init__(self, n, visibilities):
        self.correct = False
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.visibilities = visibilities

    def set_n(self, n):
        self.n = n

    def get_n(self):
        return self.n

    def set_nums(self, numbers):
        self.board = numbers

    def get_nums(self, numbers):
        return self.board

    def print_board(self):
        board = [[' ' for _ in range(self.n+2)]
                    for _ in range(self.n+2)]

        # center
        for i in range(1, self.n+1):
            for j in range(1, self.n+1):
                board[i][j] = self.board[i-1][j-1]

        # add visibilities on sides
        for i in range(2*(math.ceil(self.n /2))):
            self.visibilities[i][1] += 1
            if self.visibilities[i][2] == 'left':
                board[self.visibilities[i][1]][0] = self.visibilities[i][0]
            if self.visibilities[i][2] == 'right':
                board[self.visibilities[i][1]][self.n + 1] = self.visibilities[i][0]
            if self.visibilities[i][2] == 'top':
                board[0][self.visibilities[i][1]] = self.visibilities[i][0]
            if self.visibilities[i][2] == 'bottom':
                board[self.n + 1][self.visibilities[i][1]] = self.visibilities[i][0]

        print("SOLUTION:\n")
        for i in range(self.n+2):
            for j in range(self.n+2):
                print(board[i][j], end = " ")
            print()

    def print_constraints(self):
        for i in range(len(self.visibilities)):
            print("\nConstraint ", i, ":")
            for j in range(len(self.visibilities[i])):
                print(self.visibilities[i][j], end = " ")

    def is_latin_square_valid(self, row, column):
        val = self.board[row][column]
        for i in range(self.n):
            if self.board[row][i] == val:
                return False
        for i in range(self.n):
            if self.board[i][column] == val:
                return False
        return True

    def check_constraint_row(self, row, visibilities):
        for i in range((2*math.ceil((self.n)/2))):
            if visibilities[i][1] != row:
                continue
            if visibilities[i][2] == 'left':
                pyramids = 1
                for i in range(self.n-1, 0, -1):
                    if self.board[row][i] < self.board[row][i-1]:
                        pyramids += 1
                    else:
                        break
                if pyramids != visibilities[i][0]:
                    return False
            if visibilities[i][2] == 'right':
                pyramids = 1
                for i in range(self.n-1):
                    if self.board[row][i] < self.board[row][i+1]:
                        pyramids += 1
                    else:
                        break
                if pyramids != visibilities[i][0]:
                    return False
            return True

    def check_constraint_column(self, col, visibilities):
        for i in range((2*math.ceil(self.n/2))):
            if visibilities[i][2] == 'top' or 'bottom' and visibilities[i][1] == col:
                return True
            return False

        for i in range((2*math.ceil(self.n/2))):
            if visibilities[i][1] != col:
                continue
            if visibilities[i][2] == 'left':
                pyramids = 1
                for j in range(self.n-1, 0, -1):
                    if self.board[col][j] < self.board[col][j-1]:
                        pyramids += 1
                    else:
                        break
                if pyramids != visibilities[i][0]:
                    return False
            if visibilities[i][2] == 'right':
                pyramids = 1
                for j in range(self.n-1):
                    if self.board[col][j] < self.board[col][j+1]:
                        pyramids += 1
                    else:
                        break
                if pyramids != visibilities[i][0]:
                    return False
            return True
