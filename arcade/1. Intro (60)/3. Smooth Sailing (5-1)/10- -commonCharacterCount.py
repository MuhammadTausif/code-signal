"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

my_solution = lambda s1, s2: sum([min(s1.count(i), s2.count(i)) for i in set(s1)])

def solution(s1, s2):
    com = [min(s1.count(i), s2.count(i)) for i in set(s1)]
    return sum(com)

def solution(s1, s2):
    return sum(min(s1.count(x), s2.count(x)) for x in set(s1))


def solution(s1, s2):
    count = 0
    commons = set(s1) & set(s2)
    for i in commons:
        count += min(s1.count(i), s2.count(i))
    return count


from collections import Counter


def solution(s1, s2):
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    intersection = counter1 & counter2

    return sum(intersection.values())


def solution(s1, s2):
    l1 = list(s1)
    l2 = list(s2)

    count = 0
    for c in l1:
        if c in l2:
            count += 1
            l2.remove(c)

    return count

def solution(s1, s2):
    return sum(min(s1.count(i), s2.count(i)) for i in set(s1))

import re
def solution(s1, s2):
    c = 0
    for i in s1:
        if i in s2:
            c += 1
            s2 = re.sub(i, '', s2, count=1)

    return c


def solution(s1, s2):
    d1 = dict()
    for ch in s1:
        if ch in d1:
            d1[ch] += 1
        else:
            d1[ch] = 1

    count = 0
    for ch in s2:
        if (ch in d1) and d1[ch] > 0:
            count += 1
            d1[ch] -= 1

    return count


def solution(s1, s2):
    count = 0
    stringArray = list(s2)

    for i in range(len(s1)):
        for e in range(len(stringArray)):
            if stringArray[e] == s1[i]:
                count += 1
                stringArray.pop(e)
                break

    return count

