"""
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be solution(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be solution(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be solution(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.
"""

import string
def solution(inputString):
    r = [inputString.count(i) for i in string.ascii_lowercase]
    return r[::-1] == sorted(r)

def solution(s):
    l = [s.count(i) for i in string.ascii_lowercase[::-1]]
    return l == sorted(l)

def solution(inputString):
    al = 'abcdefghijklmnopqrstuvwxyz'
    return all(inputString.count(a) >= inputString.count(b) for a, b in  zip(al, al[1:]))

import string as str
def solution(inputString):
    alph = str.ascii_lowercase
    curCount = inputString.count(alph[0])
    for i in alph[1:]:
        if inputString.count(i) > curCount:
            return False
        else:
            curCount = inputString.count(i)
    return True

def solution(inputString):
    prev = 50
    for i in string.ascii_lowercase:
        letter = inputString.count(i)
        if letter>prev: return False
        prev = letter
    return True