"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
Example

For s = "aabbbc", the output should be
solution(s) = "2a3bc".
"""

from itertools import groupby

def solution(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x

import re
def solution(s):
    counted = re.findall(r'((\w)\2*)', s)
    return "".join([ str(len(count[0])) + count[1] if len(count[0]) > 1 else str(count[0]) for count in counted])


def solution(s):
    o = ""
    c = s[0]
    i = 1
    for x in s[1::]:
        if x == c:
            i += 1
        else:
            o += (str(i) + c) if i > 1 else c
            c = x
            i = 1

    o += (str(i) + c) if i > 1 else c
    return o

def solution(s):
    c = 1
    final = ""
    last = s[0]
    for i in range(1, len(s)):
        if last == s[i]:
            c += 1
        else:
            if c > 1:
                final += str(c) + last
            else:
                final += last
            last = s[i]
            c = 1
    return final + (str(c) if c > 1 else "") + last

def solution(s):
    l, ss = [], ""
    for i,j in enumerate(s):
        if i==0: ss=j
        elif s[i-1]==j: ss+=j
        else:
            l.append(ss)
            ss = j
        if i==len(s)-1: l.append(ss)
    return "".join([str(i.count(i[0]))+i[0] if i.count(i[0])>1 else i[0] for i in l])

def solution(s):
    news=""
    while True:
        if len(s)==0: return news
        f= s[0]
        l=len(s)
        s = re.sub("^"+f+"*","",s)
        if l - len(s)>1: news += str(l- len(s)) + f
        else: news += f

def solution(s):
    temp = ""
    prev = ""
    result = ""
    for i in s:
        if temp == "" or prev == i:
            temp = temp + i
        else:
            temp = temp + "-" + i
        prev = i
    list = temp.split("-")
    for j in list:
        if len(j) == 1:
            result = result + j
        else:
            count = str(len(j))
            result = result + count + j[0]
    return result