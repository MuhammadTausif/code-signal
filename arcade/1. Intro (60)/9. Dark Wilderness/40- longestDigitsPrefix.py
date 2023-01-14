"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".
"""

import re
def solution(inputString):
    return re.findall('^\d*',inputString)[0]

import re
solution = lambda s: (re.findall("^[0-9]+", s) + [""])[0]

def solution(st):
    s = "".join([i if i.isdigit() else "-" for i in st])
    return s[:s.find("-")] if s.find("-")!=-1 else s

def solution(st):
    s = "".join([i if i.isdigit() else "-" for i in st])
    return s[:s.find("-")] if s.find("-")!=-1 else s

def solution(inputString):
    ans=""
    data="0123456789"
    for i in inputString:
        if i not in data:
            return ans
        ans+=i
    return ans

def solution(s):
    f = s + " "
    r = 0
    while f[r].isdigit() or r > len(s):
        r += 1
    return s[:r]

def solution(inputString):
    return re.search(r'^(\d+)*', inputString).group()

def solution(i):
    for x in range(len(i)):
        if i[x].isdigit()==False:
            return i[:x]
    return i

import re
def solution(inputString):
    p = r"[0-9]+"
    try:
        return re.match(p,inputString).group()
    except AttributeError:
        return ""