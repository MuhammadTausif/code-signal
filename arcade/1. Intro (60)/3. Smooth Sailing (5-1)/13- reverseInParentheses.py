"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""

def solution(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s

# props to vanpet90 for his genious idea to use eval in the previous version of this task
def solution(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


def solution(inputString):
    stack = []
    for x in inputString:
        if x == ")":
            tmp = ""
            while stack[-1] != "(":
                tmp += stack.pop()
            stack.pop()  # pop the (
            for item in tmp:
                stack.append(item)
        else:
            stack.append(x)

    return "".join(stack)

def solution(s):
    end = s.find(")")
    start = s.rfind("(",0,end)
    if end == -1:
        return s
    return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])

def solution(s):
    def helper(s):
        for i, j in enumerate(s):
            if j == "(":
                left = i
            elif j == ")":
                right = i
                return helper(s[:left] + s[left + 1: right][::-1] + s[right + 1:])
        return s
    return helper(s)

repl = lambda m: m.group(1)[::-1] if m else None

import re
def solution(s):
    while True:
        s = re.sub(r"\(([^\(]*?)\)",repl,s)
        if not re.search(r"\(",s):
            return s


def solution(inputString):
    while '(' in inputString:
        lo = inputString.rindex('(')
        fc = inputString.index(')', lo+1)
        inputString = inputString[:lo] + inputString[lo+1:fc][::-1] + inputString[fc+1:]
    return inputString

def solution(s):
    for i in range(len(s)):
            if s[i] == "(":
                start = i
            if s[i] == ")":
                end = i
                return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s

def solution(s):
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')