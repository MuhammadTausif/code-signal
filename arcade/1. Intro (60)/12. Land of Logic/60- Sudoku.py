"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = true;

For
grid = [[8, 3, 6, 5, 3, 6, 7, 2, 9],
        [4, 2, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 1, 2, 1, 4, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
These examples are represented on the image below.

all([sorted(grid[i]) == list(range(1,10)) for i in range(len(grid))])
all([sorted([grid[j][i] for j in range(len(grid[i]))]) == list(range(1,10)) for i in range(len(grid))])

[[(j,i) for i in range(0,9,3)] for j in range(0, 9, 3)]
[[g(j,i) for i in range(0,9,3)] for j in range(0, 9, 3)]
g = lambda k,l:[grid[j][i] for i in range(k,k+3) for j in range(l,l+3)]
[grid[j][i] for i in range(0,3) for j in range(0,3)]
"""
import numpy

def solution(grid):
    def r(i):
        return sorted(grid[i]) != list(range(1, 10))
    def c(i):
        return sorted([grid[x][i] for x in range(9)]) != list(range(1, 10))
    def g(x, y):
        return sorted([grid[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]) != list(range(1, 10))

    for i in range(9):
        if r(i) or c(i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if g(i, j):
                return False
    return True

def solution(grid):
    grid = numpy.array(grid)
    for i in range(3):
        for j in range(3):
            k = j + 3*i
            if len(numpy.unique(grid[k,:])) < 9:
                return False
            if len(numpy.unique(grid[:,k])) < 9:
                return False
            if len(numpy.unique(grid[3*i:3*i+3,3*j:3*j+3])) < 9:
                return False
    return True

def solution(grid):
    columnum = 0
    row = all([len(set(x))==9 for x in grid])
    column = all([len(set([grid[y][x] for y in range(9)]))==9 for x in range(9)])
    sub_grid = all([len(set([grid[y+columnum*3][x+rownum*3] for y in range(3) for x in range(3)]))==9 for rownum in range(3) for columnum in range(3)])
    return all((row,column,sub_grid))

def solution(grid):
    for i in range(9):
        if sorted(grid[i]) != list(range(1, 10)):
            return False
        if sorted([grid[j][i] for j in range(9)]) != list(range(1, 10)):
            return False
    for i in range(3):
        for j in range(3):
            if sorted([grid[3*i+a][3*j+b] for a in range(3) for b in range(3)]) != list(range(1, 10)):
                return False
    return True

def solution(grid):
    from itertools import product
    start = list(product(list(range(0, 9, 3)), list(range(0, 9, 3))))
    return all([len(set(line)) == 9 for line in grid] + [len(set(line)) == 9 for line in zip(*grid)] + [len(square) == 9 for square in (map(set, [[element for sublist in x for element in sublist] for x in [flat for flat in [[row[j:j+3] for row in grid[i:i+3]] for i, j in product(range(0, 9, 3), range(0, 9, 3))]]]))])
