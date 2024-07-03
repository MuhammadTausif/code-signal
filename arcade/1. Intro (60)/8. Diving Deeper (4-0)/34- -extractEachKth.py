"""
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
"""

s = lambda i, k:[v for i, v in enumerate(i) if (i+1) % k]

def solution(inputArray, k):
    del inputArray[k-1::k]
    return inputArray


def solution(inputArray, k):

    return [i for (n,i) in enumerate(inputArray) if (n+1) % k != 0]

def solution(inputArray, k):
    return [j for i, j in enumerate(inputArray) if (i+1) % k]

def solution(inputArray, k):
    return [inputArray[x-1] for x in range(1,len(inputArray)+1) if x%k != 0]

def solution(inputArray, k):
    answer = []
    for i in range(len(inputArray)):
        if (i + 1) % k != 0:
            answer.append(inputArray[i])
    return answer

def solution(inputArray, k):
    return [el for i, el in enumerate(inputArray) if (i + 1) % k]

def solution(i, k):
    del i[k-1::k]
    return i


def solution(inputArray, k):
    arr = []
    for x in range(len(inputArray)):
        if ((x + 1) % k != 0):
            arr.append(inputArray[x])
    return arr

def solution(inputArray, k):
    del inputArray[(k - 1)::k]
    return inputArray

def solution(inputArray, k):
    return [inputArray[i - 1] for i in range(1,len(inputArray) + 1) if i % k != 0]


