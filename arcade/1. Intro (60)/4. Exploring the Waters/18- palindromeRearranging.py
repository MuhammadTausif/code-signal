"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""

def solution(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1

def solution(inputString):
    # count the number of each individual character
    # can form a palindrome only if:
    #   at most one of the character counts is odd, all others must be even

    l = list(inputString)
    chars = set(l)
    counts = sum([l.count(x) % 2 for x in chars])
    return counts <= 1


def solution(inputString):
    s = set()
    for c in inputString:
        if c in s:
            s.remove(c)
        else:
            s.add(c)

    return len(s) <= 1

def solution(inputString):
    dic = {}
    for i in inputString:
        if i not in dic.keys(): dic[i] = 1
        else: dic[i] += 1
    counts = list(dic.values())
    hit = 0
    for i in counts:
        if i % 2 != 0: #odd number
            hit += 1
            if hit == 2: return False
    return True

def solution(s):
    return sum([s.count(i)%2 for i in set(s)])<=1

def solution(inputString):
    l=sorted(list(''.join(set(inputString))))
    print(l)
    print(len(l))
    c=0
    for i in range(len(l)):
        if inputString.count(l[i])%2!=0:
            c+=1
            print(c)
            if c>1:
                return False
    return True


def solution(inp):
    return sum([inp.count(i) % 2 for i in set(inp)]) < 2

from collections import Counter
def solution(inputString):
    c = Counter(inputString)
    e = 0
    for val in c.values():
        if val % 2 == 1:
            e += 1
    return e < 2


def solution(inputString):
    chars_set = set(inputString)
    counter = 0
    for e in chars_set:
        if inputString.count(e) % 2 != 0:
            counter += 1
        if counter > 1:
            return False

    return True


def solution(inputString):
    char_occur = {}

    for c in inputString:
        if c not in char_occur:
            char_occur[c] = 1
        else:
            char_occur[c] += 1

    odd_occ = [l for l in char_occur if char_occur[l] % 2]
    if len(odd_occ) > 1:
        return False
    else:
        return True