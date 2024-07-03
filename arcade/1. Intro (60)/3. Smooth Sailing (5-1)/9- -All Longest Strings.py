"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
"""

my_solution = lambda y: [i for i in y if len(i) == len(max(y, key=len))]

def solution(inputArray):
    m = max(len(s) for s in inputArray)
    r = [s for s in inputArray if len(s) == m]
    return r

def solution(inputArray):
    return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]

def solution(inputArray):
    longest = 0
    res = []
    for s in inputArray:
        if len(s) == longest:
            res.append(s)
        if len(s) > longest:
            longest = len(s)
            res = [s]
    return res

def solution(inputArray):
    maxLen = len(max(inputArray, key=len))
    return [ str for str in inputArray if len(str) == maxLen ]

def solution(inputArray):
    return [i for i in inputArray if len(i) == max([len(i) for i in inputArray])]

def solution(list):
   list = sorted(list, key=len, reverse=True)
   return [x for x in list if len(x) == len(list[0])]

def solution(inputArray):
    return list(filter(lambda s: 1 if len(s) == len(max(inputArray, key=len)) else 0, inputArray))

def solution(inputArray):
    d = {}
    for s in inputArray:
        if len(s) in d:
            d[len(s)].append(s)
        else:
            d[len(s)] = [s]

    return d[max(d.keys())]

def solution(inputArray):
    return [i for i in inputArray if len(i) == len(max(inputArray, key=len))]


def solution(inputArray):
    maxLen = max(inputArray, key=len)
    return [x for x in inputArray if len(x) == len(maxLen)]
