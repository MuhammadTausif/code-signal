"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.

Check out the image below for better understanding:
"""

def solution(inputArray):
    c = 2
    while True:
        if sorted([i%c for i in inputArray])[0]>0:
            return c
        c += 1


def solution(inputArray):
    i = 2
    while True:
        if all(x % i != 0 for x in inputArray):
            return i
        i = i + 1

def solution(inputArray):
    return min([i for i in range(2, max(inputArray)+2) if all([j%i!=0 for j in inputArray])])


def solution(a):
    i = 2
    while True:
        if all([n % i != 0 for n in a]):
            return i
        i += 1


def solution(inputArray):
    for i in range(2, max(inputArray) + 2):
        if i not in inputArray and all(j % i != 0 for j in inputArray):
            return i

def solution(inputArray):
    for n in range(1, max(inputArray)):
        if all(i % n for i in inputArray):
            return n
    return max(inputArray) + 1

def solution(inputArray):
    found = False
    i = 1
    while not found:
        if any(num%i==0 for num in inputArray):
            i+=1
        else:
            found = True
    return i

def solution(inputArray):

    i=0
    increment=1
    while(i<max(inputArray)):
        i+=increment
        if i in inputArray:
            i=0
            increment+=1
    return increment

def solution(ia):
    d=2
    while True:
        if all(x%d!=0 for x in ia):
            return(d)
        d+=1


def solution(inputArray):
    axis_len = max(inputArray)
    a = [False] * (axis_len + 1)
    for i in inputArray:
        a[i] = True
    i = 2
    while True:
        if all(a[j] is False for j in range(i, len(a), i)):
            return i
        i += 1







