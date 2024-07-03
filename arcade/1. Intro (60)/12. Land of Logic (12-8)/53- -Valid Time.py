"""
Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
solution(time) = true;
For time = "25:51", the output should be
solution(time) = false;
For time = "02:76", the output should be
solution(time) = false.
"""
# - -
l = lambda t: len([0<=int(t.split(':')[0])<=23 , 0<=int(t.split(':')[1])<=59]) == 2 and all([0<=int(t.split(':')[0])<=23])

def solution(time):
    h,m=map(int,time.split(":"))
    return 0<=h<24 and 0<=m<60

import time as t
def solution(time):
    try: t.strptime(time, "%H:%M")
    except: return False
    return True

def solution(time):
    return int(time[0:2]) < 24 and int(time[3:]) < 60

def solution(time):
    return int(time[:2])<24 and int(time[3:])<60

def solution(time):
    dd,mm=map(int,time.split(':'))
    return 0<=dd<24 and 0<=mm<60

def solution(t):
    return 0<=int(t[0:2])<24 and 0<=int(t[3:])<60

def solution(time):
    return(0<=int(time[0:2])<24 and 0<=int(time[3:5])<60)

def solution(time):
    return int(time[0:2]) < 24 and int(time[3:5]) < 60