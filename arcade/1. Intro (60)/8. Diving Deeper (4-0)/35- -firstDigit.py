"""
Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
solution(inputString) = '1';
For inputString = "q2q-q", the output should be
solution(inputString) = '2';
For inputString = "0ss", the output should be
solution(inputString) = '0'.
"""

def solution(inputString):
    for i in inputString:
        if i.isdigit():
            return i

import re
def solution(inputString):
    return re.findall('\d', inputString)[0]

def solution(s):
    for i in s:
        try:
            x=int(i)
            return i
        except:
            continue

import re
def solution(s):
    return re.search('\\d', s).group(0)


def solution(i):
    for x in i:
        if x.isdigit() == True:
            return x


def solution(inputString):
    for char in inputString:
        if char.isdigit():
            return char
    return 0

def solution(inputString):
    return re.findall('\d+', inputString)[0][0]


def solution(inputString):
    for i in inputString:
        if ord(i) >= 48 and ord(i) <= 57:
            return i


def solution(inputString):
    print(inputString.isdigit())
    for i in inputString:
        n = str(i)
        print(n.isdigit())
        if n.isdigit():
            return i

def solution(inputString):
    for i in inputString:
        if i.isdigit():
            return i

