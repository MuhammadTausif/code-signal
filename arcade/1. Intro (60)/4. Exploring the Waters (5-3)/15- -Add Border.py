"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]

['*'*(len(p[0])+2)]+['*'+i+'*' for i in p]+['*'*(len(p[0])+2)]
"""


def solution(picture):
    l = len(picture[0]) + 2
    return ["*" * l] + [x.center(l, "*") for x in picture] + ["*" * l]


def solution(picture):
    r = ['*' * (len(picture[0]) + 2)]
    for i in picture:
        r.append('*' + i + '*')
    r.append(r[0])
    return r

def solution(p):
    return ["*"*(len(p[0])+2)]+["*"+i+"*" for i in p]+["*"*(len(p[0])+2)]

def solution(pic):
    return ['*'*(len(pic[0]) + 2)] + \
           ['*' + i + '*' for i in pic] + \
           ['*'*(len(pic[0]) + 2)]


def solution(picture):
    picture = list(map(lambda x: "*" + x + "*", picture))
    picture.insert(0, "*" * len(picture[0]))
    picture.append("*" * len(picture[0]))
    return picture


def solution(picture):
    length = len(picture[0]) + 2
    for i in range(len(picture)):
        picture[i] = '*' + picture[i] + '*'
    picture.insert(0, '*' * length)
    picture.append('*' * length)
    return picture

def solution(picture):
    str = "*" * len(picture[0])
    picture.insert(0, str)
    picture.append(str)
    for s in range(len(picture)):
        picture[s] = "*" + picture[s] + "*"
    return picture

def solution(picture):
    for i in range(len(picture)):
        picture[i]='*'+picture[i]+'*'
    picture.insert(0,'*'*(int(len(picture[0]))))
    picture.append('*'*(int(len(picture[0]))))
    return(picture)

def solution(picture):
    picture.insert(0, '*'*(len(picture[0])+2))
    picture.insert(int(len(picture)), '*'*(int(len(picture[1])+2)))
    for x in range(1, int(len(picture))-1):
        picture[x]='*'+picture[x]+'*'
    return picture

def solution(picture):
    picture = [ '*'+ i +'*' for i in picture]
    picture = ['*'*len(picture[0])] + picture + ['*'*len(picture[0])]
    return picture





