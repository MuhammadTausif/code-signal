"""
You have deposited a specific amount of money into your bank account.
 Each year your balance increases at the same growth rate.
 With the assumption that you don't make any additional deposits,
 find out how long it would take for your balance to pass a specific threshold.

Example

For deposit = 100, rate = 20, and threshold = 170, the output should be
solution(deposit, rate, threshold) = 3.

Each year the amount of money in your account increases by 20%.
 So throughout the years, your balance would be:

year 0: 100;
year 1: 120;
year 2: 144;
year 3: 172.8.
Thus, it will take 3 years for your balance to pass the threshold, so the answer is 3.
"""

# - -
def s(d,r,t):
    c = 0
    while d<t:            
        d = d + (d*r)/100
        c = c+1 
    return c

import math
def solution(deposit, rate, threshold):
    return math.ceil(math.log(threshold/deposit, 1+rate/100))

def solution(deposit, rate, threshold):
    year = 0
    while deposit < threshold:
        deposit += deposit * rate/100
        year += 1
    return year

def solution(d, r, t):
    c = 0
    while d<t:
        c += 1
        d += d*(r/100)
    return c

def solution(deposit, rate, threshold):
    counter = 0
    while deposit < threshold:
        deposit = deposit + deposit*rate/100
        counter+=1
    return counter

from math import log, ceil
def solution(deposit, rate, threshold):
    return ceil(log(threshold/deposit, 1+rate/100))


def solution(d,r,t):
    i=0
    while t>d:
        d=d+d*(r/100)
        i+=1
    return i

def solution(deposit, rate, threshold):
    numberofyears=1
    while (deposit*(1+rate/100)**numberofyears)<threshold:
        numberofyears+=1
    return numberofyears


def solution(deposit, rate, threshold):
    count = 0
    while deposit < threshold:
        deposit += deposit * (rate / 100)
        count += 1

    return count

def solution(deposit, rate, threshold):
    contador = 0
    while (deposit < threshold):
        deposit += (rate * deposit) / 100
        contador += 1
    return contador

def solution(deposit, rate, threshold):
    count = 0
    while deposit < threshold:
        deposit *= 1 + (rate / 100)
        count += 1
    return count


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}