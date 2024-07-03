"""
Given a string, your task is to replace each of its characters
 by the next one in the English alphabet; i.e. replace a with b, replace b with c,
 etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".
"""

# - - 
l = lambda s: ''.join([chr(ord(i)+1) if i!='z' else 'a' for i in s])

def solution(s):
    return "".join(chr((ord(i)-96)%26+97) for i in s)

def solution(inputString):
    return ''.join((chr(ord(i)+1) if i!="z" else "a" for i in inputString))

from string import ascii_lowercase as a
def solution(s):
    return "".join([a[a.find(i)-25] for i in s])

from string import ascii_lowercase

def solution(inputString):
    c = {x: y for x, y in zip(ascii_lowercase, ascii_lowercase[1:] + ascii_lowercase[:1])}
    return inputString.translate(str.maketrans(c))

def solution(inputString):
    return "".join('a' if c=='z' else chr(ord(c)+1) for c in inputString)

def solution(i):
    i=list(i)
    for x in range(len(i)):
        if i[x]=='z':
            i[x]='a'
            continue
        i[x]=chr(ord(i[x])+1)
    return "".join(i)


import string


def solution(inputString):
    alph = string.ascii_lowercase

    out = ''

    for i in inputString:
        out += alph[(alph.find(i) + 1) % len(alph)]

    return out


def solution(inputString):
    return "".join( [ 'a' if c=='z' else chr(ord(c)+1) for c in inputString ] )


import string

def solution(inputString):
    allowed_signs = string.ascii_lowercase + "a"
    return "".join(allowed_signs[1 + allowed_signs.find(letter)] for letter in inputString)


def solution(inputString):
    out = ''
    for i in range(0, len(inputString)):
        if inputString[i] == 'z':
            out += 'a'
        else:
            out += chr(ord(inputString[i]) + 1)

    return out

