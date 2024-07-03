"""
You are given an array of integers.
 On each move you are allowed to increase exactly one of its element by one.
 Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.
"""

def solution(inputArray):
    a = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            f = (inputArray[i - 1] - inputArray[i]) + 1
            inputArray[i] = inputArray[i - 1] + 1
            a += f
    return a


def solution(inputArray):
    target = inputArray[0] - 1
    steps = 0

    for i in inputArray:
        if i > target:
            target = i
        else:
            target = target + 1
            steps += target - i

    return steps


def solution(inputArray):
    k = [inputArray[0]]
    for i in range(1, len(inputArray)):
        h = max(inputArray[i], inputArray[i - 1] + 1, k[i - 1] + 1)
        k.append(h)
    return sum(k) - sum(inputArray)


def solution(inputArray):
    tmp = inputArray[0]
    cnt = 0

    for v in inputArray[1:]:
        if not v > tmp:
            cnt += tmp - v + 1
            tmp += 1

        else:
            tmp = v

    return cnt


def solution(inputArray):
    r = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i + 1] <= inputArray[i]:
            d = inputArray[i] - inputArray[i + 1] + 1
            r += d
            inputArray[i + 1] += d

    return r

def solution(inputArray):
    #Compare x[i] to x[i+1].
    #If x[i] < x[i+1], pass.
    #Else, find the difference x[i]+1-x[i+1].  Add this
    #difference to total and then set x[i+1] to x[i]+1
    x, total = inputArray, 0
    for i in range(len(x)-1):
        a,b = x[i], x[i+1]
        if a >= b:
            total += a + 1 - b
            x[i+1] = a + 1
    return total


def solution(inputArray):
    count = 0

    for i in range(1, len(inputArray)):
        while inputArray[i] <= inputArray[i - 1]:
            count += inputArray[i - 1] + 1 - inputArray[i]
            inputArray[i] = inputArray[i - 1] + 1

    return count

def solution(a):
    l=len(a)
    cont=0
    for i in range (l-1):
        if a[i]>=a[i+1]:
            cont=cont+1+abs(a[i]-a[i+1])
            a[i+1]=a[i+1]+1+abs(a[i]-a[i+1])
    return cont

def solution(inputArray):
    a = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            f = (inputArray[i - 1] - inputArray[i]) + 1
            inputArray[i] = inputArray[i - 1] + 1
            a += f
    return a


def solution(inputArray):
    count = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] < inputArray[i - 1]:
            diff = inputArray[i - 1] - inputArray[i]
            count += diff + 1
            inputArray[i] += diff + 1
        elif inputArray[i] == inputArray[i - 1]:
            inputArray[i] += 1
            count += 1
        if inputArray[i] > inputArray[i - 1]:
            continue
    return count

