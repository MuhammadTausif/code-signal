"""
Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""


def solution(a):
    l = sorted([i for i in a if i > 0])
    for n, i in enumerate(a):
        if i == -1:
            l.insert(n, i)
    return l

def solution(a):
    people = sorted(filter(lambda x: x != -1, a))
    return [people.pop(0) if i != -1 else -1 for i in a]

def solution(a):
    people = [n for n in a if n != -1]
    people.sort()
    for i in range(len(a)):
        a[i] = people.pop(0) if a[i] != -1 else a[i]
    return a

def solution(a):
    l = sorted([i for i in a if i != -1])
    for i in [i for i, j in enumerate(a) if j == -1]: l.insert(i,-1)
    return l

def solution(a):
    for num in range(len(a)):
        if (a[num] == -1):
            'Leave the trees at the same place'
            continue
        for ber in range(len(a)):
            'Sort the heights by swapping if needed'
            if (a[num] < a[ber]):
                a[num], a[ber] = a[ber], a[num]
    return a


def solution(a):
    people = iter(sorted(filter(lambda m: m != -1, a)))
    return list(map(lambda x: x if x == -1 else people.__next__(), a))

def solution(a):
    humans = sorted([x for x in a if x != -1])
    output = [humans.pop(0) if a[x]!=-1 else -1 for x in range(0,len(a))]
    return(output)

def solution(a):
    a_prime = [i for i in a if i!= -1]
    a_prime = sorted(a_prime)
    j = 0
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = a_prime[j]
            j+=1
    return a

def solution(a):
    people = sorted(filter(lambda x: x >= 0, a), reverse=True)
    return [v if v < 0 else people.pop() for v in a]

def solution(a):
    b = list(filter(lambda i: i != -1,a))
    b = sorted(b)

    for index in range(0, len(a)):
        if a[index] != -1:
            a[index] = b.pop(0)
    return a



