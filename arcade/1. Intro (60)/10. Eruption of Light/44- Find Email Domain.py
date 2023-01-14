"""
An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.

Example

For address = "prettyandsimple@example.com", the output should be
solution(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be
solution(address) = "codesignal.com".
"""

def solution(address):
    return address[address.rfind('@') + 1:]

def solution(a):
    return a[a.rfind("@")+1:]

def solution(address):
    a = address.split('@')
    return a[-1]

def solution(address):
    return address.split('@')[-1]

def solution(address):
    return address[address.rindex('@') + 1:]

import re
def solution(address):
    return re.findall('@([^@]+$)', address)[0]

def solution(a):
    return a.split('@')[-1]

