"""
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
solution(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
solution(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
solution(inputString) = false.
"""

import re
def solution(s):
    return bool(re.match(('^' + '[\dA-F]{2}-' * 6)[:-1] + '$', s))

def solution(inputString):
    try:
        all = inputString.split('-')
        if len(all) !=6:
            return False
        for s in all:
            if len(s) != 2:
                return False
            int(s,16)
        return True
    except:
        return False


import re
def solution(inputString):
    return re.match("^([0-9A-F]{2}-){5}[0-9A-F]{2}$", inputString) is not None

def solution(inputString):
    return bool(re.match('^([0-9A-F]{2}-){5}([\dA-F]{2})$', inputString))

def solution(s):
    l = s.split("-")
    if len(l)!=6: return False
    for i in l:
        if len(i)!=2: return False
        try: int(i,16)
        except: return False
    return True

def solution(inputString):
    return bool(re.fullmatch(r'([A-F\d]{2}-){5}([A-F\d]{2})', inputString))

def solution(inputString):
    addr = inputString.split('-')
    return len(addr) == 6 and all(map(lambda x: len(x) == 2 and all(l in string.hexdigits for l in x), addr))

