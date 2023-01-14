"""
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.

Example

For n = 152, the output should be
solution(n) = 52;
For n = 1001, the output should be
solution(n) = 101.
"""

def solution(n):
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))

def solution(n):
    return max([int(str(n)[:i] + str(n)[i+1:]) for i in range(len(str(n)))])

def solution(n):
    return max(int(str(n)[:i] + str(n)[i+1:]) for i in range(len(str(n))))

from itertools import combinations
def solution(n):
    return int(max(''.join(el) for el in combinations(str(n), len(str(n))-1)))


def solution(n):
    n = str(n)
    highest = 0
    counter = 0
    placeholder = ""
    joined = ""
    joinvar = ""
    while (counter != len(n)):
        nlist = [i for i in n]
        nlist.pop(counter)
        joined = int(joinvar.join(nlist))
        if (joined > highest):
            highest = joined
        counter += 1
    return (highest)

def solution(n):
    ret = 0
    n = str(n)
    for i in range(len(n)):
        ret = max(ret, int(n[:i] + n[i + 1:]))
    return ret

def solution(n):
    f=[]
    for x in range(len(str(n))):
        f.append(int(str(n)[:x]+str(n)[x+1:]))
    return max(f)

def solution(n):
    n = str(n)
    return max( int( n[:i] + n[i+1:] ) for i in range(len(n)))


def solution(n):
    x = list(str(n))
    test = []
    for i in range(len(x)):
        x.pop(i)
        test.append(''.join(x))
        x = list(str(n))

    return int(max(test))

def solution(n):
    max_number = 0
    for i in str(n):
        number = list(str(n))
        number.remove(i)
        if max_number < int(''.join(number)):
            max_number = int(''.join(number))
    return max_number



