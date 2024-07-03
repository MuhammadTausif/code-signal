"""
Given an array of integers, find the maximal absolute difference between 
any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
solution(inputArray) = 3.
"""

def solution(a):
    diffs=[abs(a[i]-a[i+1]) for i in range(len(a)-1)]
    return max(diffs)

def solution(a):
    return max([abs(a[i]-a[i+1]) for i in range(len(a)-1)])

def solution(inputArray):
    return max([abs(i - j) for i, j in zip(inputArray, inputArray[1:])])

def solution(inputArray):
    return max([abs(inputArray[n]-inputArray[n-1]) for n in range(1,len(inputArray))])

def solution(inputArray):
    return max(abs(inputArray[i] - inputArray[i+1]) for i in range(len(inputArray)-1))

def solution(iA):
    mD=0
    for x in range(len(iA)-1):
        if abs(iA[x]-iA[x+1])>=mD:
            mD=abs(iA[x]-iA[x+1])
    return mD

def solution(inputArray):

    r = abs(inputArray[0] - inputArray[1])
    for i in range(1,len(inputArray)-1):
        if r < abs(inputArray[i] - inputArray[i+1]):
            r = abs(inputArray[i] - inputArray[i+1])
    return r

def solution(inputArray):
    return max(abs(a-b) for a,b in zip(inputArray, inputArray[1:]))

def solution(inputArray):
    return max([abs(t - s) for s, t in zip(inputArray, inputArray[1:])])

def solution(inputArray):
    return max([abs(inputArray[i]-inputArray[i+1]) for i in range(len(inputArray)-1)])
