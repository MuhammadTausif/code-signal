"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".
"""


def solution(st):
    for i in range(0, len(st)):
        if (st[i:len(st)] == st[i:len(st)][::-1]):
            return st[0:i] + st[i:len(st)] + st[0:i][::-1]

def solution(st):
    string_list = list(st)
    i = 0
    while string_list != string_list[::-1]:
        string_list.insert(len(st),st[i])
        i += 1
    return "".join(string_list)

def solution(s):
    for i, c in enumerate(s):
        if s == s[::-1]:
            return s
        if i == 0:
            s += s[0]
        else:
            s = s[:-i] + s[i] + s[-i:]

def solution(st):
    for i in range(len(st)+1)[::-1]:
        if st[-i:] == st[:-i-1:-1]:
            return st + st[-i-1::-1]

def solution(s):
    p=len(s)//2
    return s if s[:p] == s[:len(s)-p-1:-1] else s[0] + solution(s[1:]) + s[0]

def solution(st):
    for i in range(len(st)):
        new_word = st + st[0:i][::-1]
        if new_word == new_word[::-1]:
            return new_word


