"""
Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. In other words, find the element x in a, which minimizes the following sum:

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
(where abs denotes the absolute value)

If there are several possible answers, output the smallest one.

Example

For a = [2, 4, 7], the output should be solution(a) = 4.

for x = 2, the value will be abs(2 - 2) + abs(4 - 2) + abs(7 - 2) = 7.
for x = 4, the value will be abs(2 - 4) + abs(4 - 4) + abs(7 - 4) = 5.
for x = 7, the value will be abs(2 - 7) + abs(4 - 7) + abs(7 - 7) = 8.
The lowest possible value is when x = 4, so the answer is 4.

For a = [2, 3], the output should be solution(a) = 2.

for x = 2, the value will be abs(2 - 2) + abs(3 - 2) = 1.
for x = 3, the value will be abs(2 - 3) + abs(3 - 3) = 1.
Because there is a tie, the smallest x between x = 2 and x = 3 is the answer.
"""

def solution(A):
    return A[(len(A)-1)//2]

def solution(A):
    return A[len(A)//2-(len(A)%2==0)]

import statistics
def solution(a):
    return statistics.median_low(a)

def solution(a):
    return a[(len(a)-1)//2]


def solution(a):
    new_lst = {}
    sum1 = 0
    for i in a:
        sum1 = 0
        for j in range(len(a)):
            sum1 = sum1 + abs(a[j] - i)
        new_lst[i] = sum1

    sorted_x = sorted(new_lst.items(), key=lambda kv: kv[1])
    return sorted_x[0][0]

def solution(a):
    return a[(len(a)-1)//2]


def solution(a):
    d = {}
    for i in a:
        e = []
        for j in a:
            e.append(abs(j - i))
        d[i] = sum(e)
    return sorted(d.items(), key=lambda x: x[-1])[0][0]

def solution(a):
    ans=[]
    for i in a:
        ans.append(sum([abs(j-i) for j in a]))
    tmp=min(ans)
    return a[ans.index(tmp)]

from statistics import median_low
def solution(a):
    return median_low(a)

def solution(a):
    b=[]
    a=sorted(a)
    for i in range(len(a)):
        s=0
        for j in range(len(a)):
            s+=(abs(a[i]-a[j]))
        b.append(s)
    return(a[b.index(min(b))])






