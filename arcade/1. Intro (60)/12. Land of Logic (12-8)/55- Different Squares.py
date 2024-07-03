"""
Given a rectangular matrix containing only digits,
 calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
solution(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1
"""

def solution(matrix):
    s = set()
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
                s.add((matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]))
    return len(s)

def solution(matrix):
    matrices = []
    for i in range(len(matrix[0]) - 1):
        for j in range(len(matrix) - 1):
            sq = [matrix[j][i], matrix[j][i+1], matrix[j+1][i], matrix[j+1][i+1]]
            if sq not in matrices:
                matrices.append(sq)
    return len(matrices)


def solution(matrix):
    unique = set()
    for row in range(len(matrix) - 1):
        for col in range(len(matrix[row]) - 1):
            unique.add((matrix[row][col], matrix[row + 1][col], matrix[row][col + 1], matrix[row + 1][col + 1]))

    return len(unique)

def solution(matrix):
    n = len(matrix)
    m = len(matrix[0])
    mp = dict()
    for i in range(n - 1):
        for j in range(m - 1):
            arr = list()
            arr.append(matrix[i][j])
            arr.append(matrix[i][j + 1])
            arr.append(matrix[i + 1][j + 1])
            arr.append(matrix[i + 1][j])
            mp[tuple(arr)] = mp.get(tuple(arr), 0) + 1
    return len(mp)

def solution(matrix):
    all2x2 = set()
    for x in range(len(matrix) - 1):
        for y in range(len(matrix[0]) - 1):
            all2x2.add(tuple(matrix[x+i][y+j] for i, j in ((0,0), (0,1), (1,0), (1,1))))
    return len(all2x2)

def solution(matrix):
    return len(set(tuple(matrix[o][n] for o in range(i,i+2) for n in range(j,j+2)) for i in range(len(matrix)-1) for j in range(len(matrix[i])-1)))

