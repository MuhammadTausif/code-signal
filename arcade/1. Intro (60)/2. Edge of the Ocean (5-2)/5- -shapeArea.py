"""
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.



Example

For n = 2, the output should be
solution(n) = 5;
For n = 3, the output should be
solution(n) = 13.
"""

my_solution = lambda n: (n-1)**2 + n**2

def solution(n):
    return (n * n) + (n - 1) * (n- 1)

def solution(n):
    return n**2 + (n-1)**2

def solution(n):
    return 2*n*(n-1)+1


def solution(n):
    result = 1
    for i in range(n):
        result += 4 * i
    return result

def solution(n):
    return n ** 2 + (n-1) ** 2

def solution(n):
    a = n ** 2
    b = (n-1) ** 2
    return a+b


def solution(n):
    result = 1

    for i in range(0, n):
        result += 4 * i
    print(result)
    return (result)


