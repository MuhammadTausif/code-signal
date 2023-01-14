"""
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.



For cell1 = "A1" and cell2 = "H3", the output should be
solution(cell1, cell2) = false.


"""


def solution(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1]) + ord(cell2[0]) + int(cell2[1])) % 2 == 0

def solution(c1, c2):
    return (ord(c1[0])+int(c1[1])+ord(c2[0])+int(c2[1]))%2==0

def solution(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1]) )%2 == (ord(cell2[0]) + int(cell2[1]) )%2


def solution(cell1, cell2):
    cell1Dark = (ord(cell1[0]) % 2 == 0) != (int(cell1[1]) % 2 == 0)
    cell2Dark = (ord(cell2[0]) % 2 == 0) != (int(cell2[1]) % 2 == 0)

    return cell1Dark == cell2Dark


def solution(cell1, cell2):
    white = set(["A2", "A4", "A6", "A8",
                 "B1", "B3", "B5", "B7",
                 "C2", "C4", "C6", "C8",
                 "D1", "D3", "D5", "D7",
                 "E2", "E4", "E6", "E8",
                 "F1", "F3", "F5", "F7",
                 "G2", "G4", "G6", "G8",
                 "H1", "H3", "H5", "H7"])

    if cell1 in white and cell2 in white:
        return True
    elif cell1 not in white and cell2 not in white:
        return True
    return False

def solution(cell1, cell2):
    return color(cell1) == color(cell2)

def color(cell):
    return (charToInt(cell[0]) % 2 + int(cell[1]) % 2) % 2

def charToInt(char):
    return ord(char) - 64

def solution(cell1, cell2):
    letter1, letter2 = ord(cell1[0]), ord(cell2[0])
    num1, num2 = ord(cell1[1]), ord(cell2[1])
    result1, result2 = letter1 + num1, letter2 + num2
    if result1 % 2 == result2 % 2:
        return True
    else:
        return False

def solution(cell1, cell2):
    c1 = (ord(cell1[0]) + int(cell1[1])) % 2
    c2 = (ord(cell2[0]) + int(cell2[1])) % 2
    return c1 == c2


def solution(cell1, cell2):
    cell_black = [False, False]
    cells = [cell1, cell2]

    for i in range(2):
        if (ord(cells[i][0]) % 2 == 0) == (int(cells[i][1]) % 2 == 0):
            cell_black[i] = True

    return cell_black[0] == cell_black[1]

def solution(cell1, cell2):
    AH = "ABCDEFGH"
    num1 = AH.index(cell1[0]) + int(cell1[1])
    num2 = AH.index(cell2[0]) + int(cell2[1])
    num1 = int( str(num1/2)[2] )
    num2 = int( str(num2/2)[2] )
    return num1 == num2


