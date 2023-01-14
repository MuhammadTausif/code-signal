"""
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

Example

For inputString = "2 apples, 12 oranges", the output should be
solution(inputString) = 14.
"""

import re
def solution(inputString):
    l = re.findall(r"\d+",inputString)
    return sum([int(i) for i in l])

def solution(s):
    return sum(map(int,"".join([i if i.isdigit() else " " for i in s]).split()))

def solution(i):
    return sum(map(int,re.findall('\d+',i)))

def solution(inputString):
    return sum(map(int, re.findall(r'\d+', inputString, re.ASCII)))

def solution(s):
    return sum(map(int, re.findall(r'\d+', s)))


