"""
Given a position of a knight on the standard chessboard, 
find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally 
 and one square vertically, or two squares vertically and one square
 horizontally away from it. The complete move therefore looks like the letter L.
 Check out the image below to see all valid moves for a knight piece that is
 placed on one of the central squares.



Example

For cell = "a1", the output should be
solution(cell) = 2.



For cell = "c2", the output should be
solution(cell) = 6.

"""

def solution(c):
    x,y = ord(c[0])-96, int(c[1])
    return sum([1<=(x+i)<=8 and 1<=(y+j)<=8 for i in [-2,-1,1,2] for j in [-2,-1,1,2]])//2


def solution(cell):
    r = 0
    c = [ord(cell[0]) - 96, int(cell[1])]

    m = [[1, 2], [2, 1], [1, -2], [-2, 1], [-1, 2], [2, -1], [-1, -2], [-2, -1]]

    for i in m:
        if 0 < c[0] + i[0] < 9 and 0 < c[1] + i[1] < 9:
            r += 1
    return r


def solution(cell):
    p = 1
    if (cell[0] == "a" or cell[0] == "h"):
        p = p / 2
    if (cell[0] == "b" or cell[0] == "g"):
        p = p * 3 / 4
    if (cell[1] == "1" or cell[1] == "8"):
        p = p / 2
    if (cell[1] == "2" or cell[1] == "7"):
        p = p * 3 / 4
    if (p == 3 / 4 * 3 / 4):
        p = 1 / 2

    return p * 8

def solution(c):
    x = ord(c[0])-96
    y = int(c[1])
    d = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
    return sum(0 < x+l[0] < 9 and 0 < y+l[1] < 9 for l in d)

def solution(cell):
    dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    return sum(10 <= int(cell[0], 18) + dl <= 17 and 1 <= int(cell[1]) + dn <= 8  for dn, dl in dirs)

def solution(cell):
    pos = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
    return sum(map(lambda x: 1 <= int(cell[0], 18) - 9 + x[0] <= 8 and 1 <= int(cell[1]) + x[1] <= 8, pos))

def solution(cell):
    h= ord(cell[0]) -96
    v= int(cell[1])
    mh = min([(9-h),h])
    mv = min([(9-v),v])
    t = mh + mv
    if t in [2,3,4]:
        return t
    elif t == 5:
        if min([mh,mv]) == 1:
            return 4
        else:
            return 6
    elif t == 6 and min([mh,mv]) == 2:
        return 6
    else:
        return 8

def isValid(x,y):
    if(x>0 and x<9 and y>0 and y<9):
        return 1
    return 0
def solution(cell):
    a=ord(cell[0])-96
    b=int(cell[1])
    print(a,b)
    cnt=0
    arr=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    for i in range(8):
        cnt+=isValid(a+int(arr[i][0]),b+int(arr[i][1]))
    return cnt 

