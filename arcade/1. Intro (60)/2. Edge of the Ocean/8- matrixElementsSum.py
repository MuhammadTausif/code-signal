"""
After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
the output should be
solution(matrix) = 9.

example 1

There are several haunted rooms, so we'll disregard them as well as any rooms beneath them. Thus, the answer is 1 + 5 + 1 + 2 = 9.

For

matrix = [[1, 1, 1, 0],
          [0, 5, 0, 1],
          [2, 1, 3, 10]]
the output should be
solution(matrix) = 9.

example 2

Note that the free room in the final column makes the full column unsuitable for bots (not just the room directly beneath it). Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.
"""

s8 = lambda x: sum(x[0] + list(map(sum, [[ x[i][j] for j in range(len(x[i])) if x[i - 1][j] != 0 ] for i in range(1, len(x))])))
def my_solution1(x):
    out = x[0]
    [[out.append(x[i][j]) for j in range(len(x[i])) if x[i - 1][j] != 0] for i in range(1, len(x))]
    return sum(out)

def my_solution(x):
    out = x[0]
    for i in range(1, len(x)):
        for j in range(len(x[i])):
            if x[i - 1][j] != 0:
                out.append(x[i][j])
    return sum(out)

def solution(matrix):
    matrix = zip(*matrix)
    sum = 0
    for r in matrix:
        for c in r:
            if c > 0:
                sum = sum + c
            else:
                break
    return sum

def solution(m):
    r = len(m)
    c = len(m[0])
    total=0
    for j in range(c):
        for i in range(r):
            if m[i][j]!=0:
                total+=m[i][j]
            else:
                break
    return total

def solution(matrix):
    mt = list(zip(*matrix))
    from itertools import takewhile
    return sum([sum(takewhile(lambda x: x>0, y)) for y in mt])


def solution(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0 and i + 1 < len(matrix):
                matrix[i + 1][j] = 0
            sum += matrix[i][j]

    return sum

def solution(matrix):
    roomRents=0
    unzip = zip(*matrix)
    for i in unzip:
        for j in i:
            if(j==0):
                break
            else:
                roomRents+=j
    return roomRents

def solution(matrix):
    m = list(zip(*matrix))
    sum = 0
    for l in m:
        for n in l:
            if n == 0:
                break
            else:
                sum += n
    return sum

def solution(matrix):
    matrix=list(zip(*matrix))
    count=0
    for i in matrix:
        for j in i:
            if j==0:
                break
            count+=j
    return count

def solution(matrix):
    s = 0
    for floorNum, floor in enumerate(matrix):
        for roomNum, roomPrice in enumerate(floor):
            if floorNum > 0 and matrix[floorNum-1][roomNum] == 0:
                matrix[floorNum][roomNum] = 0
            else:
                s += roomPrice
    return s




