"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

solution(n) = [[1, 2, 3],
               [8, 9, 4],
               [7, 6, 5]]
"""

def solution(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    return m

import numpy

def nx(i, j, d):
    if d==0:
        return (i,j+1)
    if d==1:
        return (i+1,j)
    if d==2:
        return (i,j-1)
    if d==3:
        return (i-1,j)

def solution(n):
    a=numpy.zeros((n,n),dtype=int)
    d,i,j,k,l=0,0,0,0,1
    for c in range(n*n):
        a[i][j]=c+1
        i,j=k,l
        k,l=nx(i,j,d)
        if k<0 or k >=n or l<0 or l>=n or a[k][l]>0:
            d=(d+1)%4
            k,l=nx(i,j,d)
    return a

def solution1(n):
    p = [(1 if i % 2 == 0 else n)*((-1)**((i//2) % 2)) for i in range(2*n-1) for j in range(n-(i+1)//2)]
    q = [sum(p[:i+1]) for i in range(n*n)]
    r = sorted([i+1 for i in range(n*n)], key=lambda x: q[x-1])
    return [r[n*i:n*(i+1)] for i in range(n)]

def solution2(n):
    ans = [ [ 0 for j in range(n) ] for i in range(n) ]
    i = j = 0
    di, dj = 0, 1
    for v in range(1, n*n+1):
        ans[i][j] = v
        if not( 0 <= i + di < n and 0 <= j + dj < n ) or ans[i + di][j + dj] != 0:
            di, dj = dj, -di
        i += di
        j += dj
    return ans

solution2(3)
