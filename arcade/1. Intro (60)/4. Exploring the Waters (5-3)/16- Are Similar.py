"""
Two arrays are called similar if one can be obtained from another
 by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
"""

def solution(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2

from collections import Counter as C

def solution(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3


def solution(A, B):
    r = []
    for i in range(len(A)):
        if A[i] != B[i]:
            r.append([A[i], B[i]])

    if len(r) == 0 or len(r) == 2 and r[0] == r[1][::-1]:
        return True
    return False

def solution(a, b):
    same_items = sorted(a) == sorted(b)
    differences = [i for i in range(len(a)) if a[i] != b[i]]
    return len(differences) <= 2 and same_items

def solution(a, b):
    return sorted(a)==sorted(b) and sum(i!=j for i,j in zip(a,b))<3

def solution(A, B):
    if A==B:
        return True
    i = 0
    while i<len(A):
        if A[i]==B[i]:
            A.pop(i)
            B.pop(i)
        else:
            i += 1
    if len(A)!=2:
        return False
    B.reverse()
    if A==B:
        return True
    else:
        return False

from collections import Counter

def solution(a, b):
    return Counter(a) == Counter(b) and sum(x != y for x, y in zip(a, b)) <= 2

def solution(a, b):
    return (sorted(a) == sorted(b)) and (sum([first != second for first, second in zip(a, b)]) <= 2)

def solution(A, B):
    return(sorted(A) == sorted(B) and sum([a != b for a,b in zip(A, B)]) <=2)

from collections import Counter

def solution(a, b):
    return Counter(a)==Counter(b) and sum([el_a!=el_b for el_a,el_b in zip(a,b)])<=2

