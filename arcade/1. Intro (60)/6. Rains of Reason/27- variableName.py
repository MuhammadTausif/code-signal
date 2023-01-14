"""
Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
solution(name) = true;
For name = "qq-q", the output should be
solution(name) = false;
For name = "2w2", the output should be
solution(name) = false.
"""

def solution(name):
    return name.isidentifier()

import re
def solution(name):

    if re.match('[a-z_][0-9_a-z]*$', name,re.IGNORECASE):
        return True
    return False

def solution(n):
    return n.isidentifier()

def solution(name):
    if not name[0].isdigit():
        for n in name:
            if n != '_' and not n.isalpha() and not n.isdigit():
                return False
        return True
    return False


def solution(name):
    for i in name:
        if not (i.isalpha() or i.isdigit() or i == "_"):
            return False

    if name[0].isdigit():
        return False
    else:
        return True

import string
def solution(n):
    return n.isidentifier()


a = string.ascii_letters + '_' + string.digits


def solution(s):
    if s[0] in string.digits:
        return False

    for x in s:
        if x not in a:
            return False

    return True

def solution(name):
    return name.isidentifier()

def solution(name):
    return name.isidentifier()

def solution(name):
    return name.isidentifier()

