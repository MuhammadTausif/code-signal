"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.
"""
def solution(s):
    p = s.split('.')
    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

import ipaddress
def solution(inputString):
    try:
        ipaddress.ip_address(inputString)
    except:
        return False
    return True

def solution(inputString):
    l = inputString.split('.')
    if len(l) != 4:
        return False
    for i in range(len(l)):
        if not l[i].isnumeric():
            return False
        elif (len(l[i]) > 1) and (l[i][0] == '0'):
            return False
        elif int(l[i]) not in range(256):
            return False
    return True

def solution(inputString):
    l=inputString.split('.')
    if len(l)!=4:
        return False
    for i in range(len(l)):
        if l[i]=='':
            return False
        if l[i].isdecimal()==False:
            return False
        if l[i]!=str(int(l[i])):
            return False
        if int(l[i])>255:
            return False
    return True

import re
def solution(inputString):

    if re.match('\d+\.\d+\.\d+\.\d+$', inputString):
        for i in inputString.split('.'):
            if not 0<=int(i)<256:
                return False
        return True
    return False

def solution(inputString):
    numbers = inputString.split('.')
    if len(numbers) != 4:
        return False
    for number in numbers:
        if not number.isnumeric() or int(number) < 0 or int(number) > 255 or str(int(number)) != number:
            return False
    return True

def solution(inputString):
    sp = inputString.split('.')
    return len([x for x in sp if x.isdigit() and str(int(x)) == x and 0 <= int(x) <= 255 ]) == 4 and len(sp) == 4


def notNumber(a):
    # return true if this is not valid number

    for i in a:
        zero = ord('0')
        nine = ord('9')
        num = False
        for j in range(zero, nine):
            if i == j:
                num = True
        if not num:
            return False

    return False


def solution(inputString):
    segments = inputString.split('.')
    if (len(segments) != 4):
        return False

    for i in segments:
        if len(i) == 0:
            return False
        if not i.isnumeric():
            return False
        if i[0] == '0' and len(i) > 1:
            return False
        if int(i) > 255:
            return False
    return True


def solution(inputString):
    # return int(inputString.split(".")[1]) <= 255 and int(inputString.split(".")[1]) >= 0
    if '.' not in inputString:
        return False
    inputString = inputString.split(".")
    if len(inputString) == 4:
        for i in inputString:
            if i:
                try:
                    print(i,len(i),i[0])
                    if int(i) >= 0 and int(i) <= 255 and len(i)>=2 and int(i[0]) == 0:
                        return False
                    elif int(i) >= 0 and int(i) <= 255:
                        continue
                    else:
                        return False
                except Exception as e:
                    return False
            else:
                return False
    else:
        return False
    return True


import re


def solution(inputString):
    pattern = re.compile("^(\d+).(\d+).(\d+).(\d+)$")
    find = pattern.search(inputString)

    if find:
        return all(0 <= int(v) <= 255 for v in find.groups())

    else:
        return False


