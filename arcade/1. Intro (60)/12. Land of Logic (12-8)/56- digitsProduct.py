"""
Given an integer product, find the smallest positive (i.e. greater than 0)
 integer the product of whose digits is equal to product. 
 If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
solution(product) = 26;
For product = 19, the output should be
solution(product) = -1.

"""

def solution(p):
    if p == 0: return 10
    for i in range(3600):
        a = 1
        for j in str(i):
            a *= int(j)
        if a == p: return i
    return -1


import numpy as np

def solution1(product):
    for i in range(1, 10000):
        if product == np.prod(list(map(int, str(i)))):
            return i
    return -1

def solution2(product):
    if product < 10:
        return product if product > 0 else 10
    r = ""
    for i in range(9,1,-1):
        while product % i == 0:
            product /= i
            r = chr(ord('0')+i)  + r;
    return -1 if product != 1 else int(r)

def solution3(product):
    if product < 10:
        return product if product > 0 else 10
    rr = ''
    for i in range(9, 1, -1):
        while product % i == 0:
            product /= i
            rr = str(i) + rr
    return -1 if product != 1 else int(rr)

def solution4(p):
    if p<10:
        return p if p>0 else 10
    try:
        return min([int(str(i)+str(solution(p//i))) for i in range(2,10) if p%i==0])
    except ValueError:
        return -1