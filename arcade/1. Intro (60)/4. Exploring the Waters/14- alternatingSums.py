"""
Several people are standing in a row and need to be divided into two teams. The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people. Return an array of two integers, where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.

Example

For a = [50, 60, 60, 45, 70], the output should be
solution(a) = [180, 105].
"""

def solution(a):
    return [sum(a[::2]),sum(a[1::2])]

def solution(a):
    sums = [0, 0]
    for i, w in enumerate(a):
        sums[i % 2] += w
    return sums

def solution(a):
    return sum(a[::2]),sum(a[1::2])

def solution(a):
    whole = sum(a)
    first = sum (a[::2])
    result = [first, whole-first]
    return result

def solution(a):
    return [sum(a[::2]), sum(a[1::2])]

def solution(a):
    return [sum([i for i in a[::2]]), sum([i for i in a[1::2]])]

solution = lambda a: [sum(i for i in a[::2]), sum(i for i in a[1::2])]

def solution(a):
    b=[0,0]
    for i in range(len(a)):
        b[i%2]+=a[i]
    return b

def solution(a):
    return [sum(a[0::2]), sum(a[1::2])]

def solution(a):
    return [sum(a[::2]), sum(a[1::2])]

