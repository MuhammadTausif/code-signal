"""
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
solution(text) = "steady".
"""

import re
import string

def solution(text):
    return max(re.split('[^a-zA-Z]', text), key=len)

def solution_1(t):
    return max("".join([i if i in string.ascii_letters else " " for i in t]).split(),key=len)

def solution_2(text):
    return max(re.findall(r'[a-z]+', text, re.IGNORECASE), key=len)

def solution_3(text):
    return max(re.findall(r'([A-Za-z]+)', text), key=len)

def solution_4(text):
    l = re.findall(r"(?<=\b)\w+(?=\b)",text)
    return sorted(l, key=lambda x: len(x))[-1]

# UNILPKKA