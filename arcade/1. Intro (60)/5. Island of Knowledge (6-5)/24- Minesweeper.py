"""
In the popular Minesweeper game you have a board with some mines
 and those cells that don't contain a mine have a number in it that
 indicates the total number of mines in the neighboring cells. 
 Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
Check out the image below for better understanding:
"""


def solution1(matrix):
    r = []

    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[0]):
                        l += matrix[i + x][j + y]

            r[i].append(l)
    return r


def solution2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    conv = lambda i, j: 1 if 0 <= i < rows and 0 <= j < cols and matrix[i][j] else 0

    nbs = lambda i, j: sum(conv(ii, jj) for ii in range(i - 1, i + 2) for jj in range(j - 1, j + 2)) - conv(i, j)

    return [[nbs(i, j) for j in range(cols)] for i in range(rows)]


def solution3(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    ret = [[0] * cols for __ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]:
                for a in range(max(0, i - 1), min(i + 2, rows)):
                    for b in range(max(0, j - 1), min(j + 2, cols)):
                        if a != i or b != j:
                            ret[a][b] += 1
    return ret


from itertools import product


def solution4(matrix):
    H = len(matrix)
    W = len(matrix[0])
    a = [[None for _ in range(W)] for _ in range(H)]
    for i, j in product(range(H), range(W)):
        cnt = 0
        for di, dj in product([-1, 0, 1], [-1, 0, 1]):
            if di == 0 and dj == 0:
                continue
            if i + di >= 0 and j + dj >= 0 and i + di < H and j + dj < W:
                if matrix[i + di][j + dj]:
                    cnt += 1
        a[i][j] = cnt
    return a


import numpy as np


def solution5(matrix):
    matrix = np.array(matrix, 'int')
    x, y = matrix.shape
    nummatrix = np.zeros((x + 2, y + 2))
    nummatrix[1:-1, 1:-1] = matrix
    out = np.zeros((x, y))
    for i in range(3):
        for j in range(3):
            print(i, j)
            print(nummatrix[i:x + i, j:y + j].shape)
            out = out + nummatrix[i:x + i, j:y + j]
    return out - matrix


def solution6(matrix):
    return [[sum(matrix[i][j] for i in [r - 1, r, r + 1] for j in [c - 1, c, c + 1] if
                 0 <= i < len(matrix) and 0 <= j < len(matrix[0])) - matrix[r][c] for c in range(len(matrix[0]))] for r
            in range(len(matrix))]


def solution7(matrix):
    import numpy as np

    image = np.array(matrix)

    R, C = image.shape

    out = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            up = max(0, r - 1)
            down = min(r + 2, R)
            left = max(0, c - 1)
            right = min(c + 2, C)

            out[r][c] = image[up:down, left:right].sum() - image[r, c]

    return out


def solution8(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == True:
                M[i][j] = 1
            else:
                M[i][j] = 0
    A = [[0] * (len(M[0]) + 2)] + [[0] + x + [0] for x in M] + [[0] * (len(M[0]) + 2)]
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = (A[i + 0][j] + A[i + 0][j + 1] + A[i + 0][j + 2] +
                       A[i + 1][j] + 0 + A[i + 1][j + 2] +
                       A[i + 2][j] + A[i + 2][j + 1] + A[i + 2][j + 2])
    return M


def solution9(m):
    n = [[0 for x in m[0]] for y in m]
    for i in range(len(m)):
        for j in range(len(m[0])):
            t = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x <= len(m) - 1 and 0 <= y <= len(m[0]) - 1 and not (x == i and y == j):
                        if m[x][y]:  t += 1
            n[i][j] = t
    return n


def find_num_mines_around(matrix, row, col):
    try:
        if row < 0 or row > len(matrix):
            return 0
        if col > len(matrix) or col < 0:
            return 0
        if matrix[row][col] is True:
            return 1
    except IndexError:
        return 0
    return 0


def count_mine_around(matrix, row, col):
    top_r = find_num_mines_around(matrix, row - 1, col + 1)
    top = find_num_mines_around(matrix, row - 1, col)
    top_l = find_num_mines_around(matrix, row - 1, col - 1)
    r = find_num_mines_around(matrix, row, col + 1)
    bot_r = find_num_mines_around(matrix, row + 1, col + 1)
    bot = find_num_mines_around(matrix, row + 1, col)
    bot_l = find_num_mines_around(matrix, row + 1, col - 1)
    l = find_num_mines_around(matrix, row, col - 1)
    sum = top_r + top + top_l + r + bot_r + bot + bot_l + l
    print("sum:", sum)
    return sum


def solution10(matrix):
    row = len(matrix)
    col = len(matrix[0])
    res = []
    for i in range(0, row):
        temp = []
        for j in range(0, col):
            temp.append(count_mine_around(matrix, i, j))
        res.append(temp)
    return res
