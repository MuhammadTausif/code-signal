"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a",
the output should be
solution(inputString) = true.
"""

solution = lambda s: s[::-1] == s

def solution(inputString):
    return inputString == inputString[::-1]

def solution(inputString):
    for i in range(len(inputString) // 2):
        if inputString[i] != inputString[-i - 1]:
            return False
    return True

def solution(i):
    return (i==i[::-1])

def solution(inputString):
    return inputString[::-1] == inputString

