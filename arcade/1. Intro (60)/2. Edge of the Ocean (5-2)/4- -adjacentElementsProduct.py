"""
Given an array of integers, find the pair of adjacent elements that
 has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
"""

my_solution = lambda y: max([a*b for a,b in zip(y[:-1],y[1:])])

def my_solution(y):
    return max([a*b for a,b in zip(y[:-1],y[1:])])

def solution(inputArray):
    return max(inputArray[a] * inputArray[a + 1] for a in range(len(inputArray) - 1))

def solution(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

def solution(inputArray):
    return max(a * b for a, b in zip(inputArray[:-1], inputArray[1:]))

def solution(inputArray):
    best = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        temp = inputArray[i] * inputArray[i + 1]
        if temp > best:
            best = temp
    return best

def solution(inputArray):
    return max([inputArray[i] * inputArray[i-1] for i in range(1, len(inputArray))])

def solution(inputArray):
    muls = [inputArray[i] * inputArray[i+1] for i in range(len(inputArray) - 1)]
    return max(muls)

def solution(arr):
    return max(arr[i]*arr[i+1] for i in range(len(arr)-1))

def solution(inputArray):
    return max([inputArray[i]*inputArray[i+1] for i in range(len(inputArray)) if i < len(inputArray)-1])

def solution(inputArray):
    max = inputArray[0] * inputArray[1]
    for x in range(len(inputArray)-1):
        value = inputArray[x] * inputArray[x+1]
        if max < value:
            max = value
    return max