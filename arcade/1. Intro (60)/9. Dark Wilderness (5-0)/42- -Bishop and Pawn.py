"""
Given the positions of a white bishop and a black pawn on the standard chess board,
 determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move,
 but is limited to diagonal movement. Check out the example below to see how it can move:


Example

For bishop = "a1" and pawn = "c3", the output should be
solution(bishop, pawn) = true.



For bishop = "h1" and pawn = "h3", the output should be
solution(bishop, pawn) = false.

"""

def solution(bishop, pawn):
    return abs(ord(bishop[0]) - ord(pawn[0])) == abs(ord(bishop[1]) - ord(pawn[1]))

def solution(b, p):
    b=[ord(b[0]),int(b[1])]
    p=[ord(p[0]),int(p[1])]
    return b[1]-b[0]==p[1]-p[0] or sum(b)==sum(p)

def solution(bishop, pawn):
    return abs(ord(bishop[0])-ord(pawn[0]))==abs(int(pawn[1])-int(bishop[1]))


def solution(bishop, pawn):
    cols = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    if (abs(cols[bishop[0]] - cols[pawn[0]]) == abs(int(bishop[1]) - int(pawn[1]))):
        return True
    return False

def solution(bishop, pawn):
    return abs((ord(pawn[0])-ord(bishop[0]))/(int(pawn[1])-int(bishop[1]))) == 1


def solution(bishop, pawn):
    row = abs(ord(bishop[0]) - ord(pawn[0]))
    col = abs(int(bishop[1]) - int(pawn[1]))
    return row == col

def solution(bishop, pawn):
    return abs(int(bishop[1]) - int(pawn[1])) == abs(ord(bishop[0]) - ord(pawn[0]))

def solution(b, p):
    return abs((ord(b[0])-96)-(ord(p[0])-96))==abs(int(b[1])-int(p[1]))

def solution(bishop, pawn):
    colb = ord(bishop[0])
    rowb = int(bishop[1])
    colp = ord(pawn[0])
    rowp = int(pawn[1])
    if abs(colb - colp) == abs(rowb - rowp):
        return True
    else:
        return False

def solution(bishop, pawn):
    return abs(ord(bishop[0])-ord(pawn[0])) == abs(ord(bishop[1])-ord(pawn[1]))