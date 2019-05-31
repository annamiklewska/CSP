import math
import random

import board

# c [val][row][column]

'''
def generate_constraints(n):
    rows = math.ceil(n/2)
    positionsColLeftRight = [0, n+1]
    positionsRowLeftRight = [i for i in range(1, n+1)]
    positionsColTopBottom = positionsRowLeftRight
    positionsRowTopBottom = positionsColLeftRight
    c = [[0 for _ in range(3)] for _ in range(2*rows)]  # column, row
    for i in range(0, rows):  # Left Right
        c[i][0] = random.randint(1, n)
        c[i][1] = positionsRowLeftRight[random.randint(0, len(positionsRowLeftRight)-1)]  # row
        c[i][2] = positionsColLeftRight[random.randint(0, len(positionsColLeftRight)-1)]  # column
    for i in range(rows, (2*rows)):  # Left Right
        c[i][0] = random.randint(1, n)
        c[i][1] = positionsRowTopBottom[random.randint(0, len(positionsRowTopBottom)-1)]  # row
        c[i][2] = positionsColTopBottom[random.randint(0, len(positionsColTopBottom)-1)]  # column
    return c
'''

def generate_visibilities(n):
    rows = math.ceil(n / 2)
    v = [[0 for _ in range(3)] for _ in range(2 * rows)]  # column, row
    sidesLeftRight = ['left', 'right']
    sidesTopBottom = ['top', 'bottom']
    for i in range(0, rows):  # Left Right
        v[i][0] = random.randint(1, n)  # val
        v[i][1] = random.choice(range(n))  # row
        v[i][2] = random.choice(sidesLeftRight)  # side
    for i in range(rows, (2 * rows)):  # Left Right
        v[i][0] = random.randint(1, n)
        v[i][1] = random.choice(range(n))  # column
        v[i][2] = random.choice(sidesTopBottom)  # side
    return v
