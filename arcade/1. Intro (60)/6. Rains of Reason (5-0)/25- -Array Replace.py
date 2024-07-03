"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
"""

# - -
l = lambda i, r, s: [j if j != r else s for j in i]

def solution(i, e, s):
    return [x if x!=e else s for x in i]

def solution(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if x==elemToReplace else x for x in inputArray]

def solution(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if i == elemToReplace else i for i in inputArray]

def solution(inputArray, elemToReplace, substitutionElem):
    for index,element in enumerate(inputArray):
        if element == elemToReplace:
            inputArray[index] = substitutionElem
    return inputArray


def solution(array, remove, add):
    for x in range(len(array)):
        if array[x] == remove:
            array[x] = add
    return array

def solution(inputArray, elemToReplace, substitutionElem):
    return [x if x!=elemToReplace else substitutionElem for x in inputArray]

def solution(inputArray, elemToReplace, substitutionElem):
    for i, e in enumerate(inputArray):
        if e==elemToReplace:
            inputArray[i]=substitutionElem
    return inputArray

def solution(inputArray, elemToReplace, substitutionElem):
    return [x if x!=elemToReplace else substitutionElem for x in inputArray]


def solution(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if x == elemToReplace else x for x in inputArray]

def solution(inputArray, elemToReplace, substitutionElem):
    return [v if v != elemToReplace else substitutionElem for v in inputArray]



