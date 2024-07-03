"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
"""

# - -
s = lambda i, k: max([sum(i[j:j+k]) for j in range(0,len(i)-1)])

def solution(a, k):
    c = m = sum(a[:k])

    for i in range(len(a) - k):
        c = c + a[i + k] - a[i]
        m = max(c, m)

    return m

def solution(inputArray, k):
    # return max([sum(inputArray[i:k+i]) for i in range(len(inputArray) - k + 1)])
    # too slow, but works
    s = m = sum(inputArray[:k])
    for i in range(k, len(inputArray)):
        s += inputArray[i] - inputArray[i-k]
        if s > m: m = s
    return m

def solution(inputArray, k):
    tempSum = sum(inputArray[0:k])
    maxSum = tempSum
    for i in range(k, len(inputArray)):
        tempSum = tempSum - inputArray[i-k] + inputArray[i]
        maxSum = max(maxSum,tempSum)
    return maxSum


def solution(inputArray, k):
    maxS = s = sum(inputArray[:k])

    for i in range(0, len(inputArray) - k):
        s += inputArray[i + k] - inputArray[i]
        maxS = max(maxS, s)

    return maxS

def solution(a, k):
    n = len(a)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    answer = 0
    for i in range(n):
        if i + k - 1 < n:
            answer = max(answer, prefix[i + k] - prefix[i])
    return answer


def solution(inputArray, k):
    tesum = 0
    for j in range(0, k):
        tesum += inputArray[j]
    tosum = tesum
    for i in range(len(inputArray) - k):
        newsum = tesum + inputArray[i + k] - inputArray[i]
        if newsum > tosum: tosum = newsum
        tesum = newsum
    return tosum


def solution(inputArray, k):
    i = 0
    max = 0
    sum = 0
    n =  len(inputArray)
    while i < k:
        sum += inputArray[i]
        i += 1
    if sum > max:
        max = sum
    v = sum
    for j in range(k , n):
        v = v - inputArray[j - k] + inputArray[j]
        if v > max:
            max = v
    return max


def solution(A, k):
    m = sum(A[:k])
    m_s = m
    f = 0
    for x in A[k:]:
        m += x - A[f]
        f += 1
        m_s = max(m_s, m)
    return m_s


def solution(inputArray, k):
    maxSum = 0
    s = 0
    prev = inputArray[0]

    for i in range(k):
        s += inputArray[i]

    maxSum = s if s > maxSum else maxSum

    for i in range(1, len(inputArray) - k + 1):
        s = s - prev + inputArray[i + k - 1]
        maxSum = s if s > maxSum else maxSum
        prev = inputArray[i]
    return maxSum

def solution(inputArray, k):
    mxsum=0
    le=len(inputArray)
    tsum=0
    for i in range(le-k+1):
        if(i==0):
            for j in range(k):
                tsum+=inputArray[i+j]
        else:
            a=inputArray[i+k-1]-inputArray[i-1]
            tsum=tsum+a
        if(tsum>mxsum):
            mxsum=tsum
    return mxsum
