"""
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
solution(year) = 20;
For year = 1700, the output should be
solution(year) = 17.
"""


import math
def solution(year):
    return math.ceil(year / 100)

def solution(year):
    return (year + 99) // 100

def solution(year):
    return math.ceil(year/100)

def solution(year):
    return (year-1)//100+1


def solution(year):
    if year % 100 == 0:
        return (int(year / 100))
    else:
        return (int(year / 100 + 1))

def solution(year):
    return int((year - 1) / 100) + 1

def solution(year):
    return (year - 1) // 100 + 1





