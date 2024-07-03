"""
Let's define digit degree of some positive integer as the number of times
 we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
solution(n) = 0;
For n = 100, the output should be
solution(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
"""


def solution(n):
    if n < 10:
        return 0
    sumOfDigits = sum([int(i) for i in str(n)])
    return solution(sumOfDigits) + 1

def solution(n):
    d=0
    while n>=10:
        n=sum([int(i) for i in str(n)])
        d+=1
    return d

def solution(n):
    c = 0
    while n > 9:
        n = sum(int(i) for i in str(n))
        c += 1
    return c


def solution(n):
    c = 0
    while len(str(n)) > 1:
        n = sum(int(i) for i in str(n))
        c += 1
    return c

def solution(n):
    if len(str(n))<=1:
        return 0
    else:
        st = str(n)
        return 1 + solution(int(sum([int(i) for i in st])))


def solution(n, i=0):
    n = str(n)
    if len(n) == 1:
        return i
    else:
        return solution(sum((int(x) for x in n)), i + 1)

def solution(n):
  count = 0
  while n > 9:
    n = sum([int(k) for k in str(n)])
    count += 1
  return count