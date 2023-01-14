"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from  the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
"""

def solution(s):
    return 3 > sum((i >= j) + (i >= k) for i, j, k in zip(s, s[1:], s[2:] + [10**6]))

def solution(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True

def solution(sequence):
    f1 = sum([1 for a, b in zip(sequence[:-1], sequence[1:]) if a>=b ]) <= 1
    f2 = sum([1 for a, c in zip(sequence[:-2], sequence[2:]) if a>=c ]) <= 1
    return f1 and f2

def solution(sequence):
    c = 0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]: c += 1
        if i+2 < len(sequence) and sequence[i] >= sequence[i+2]: c += 1
    return c < 3

