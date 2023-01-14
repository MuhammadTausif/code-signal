"""
Determine if the given character is a digit or not.

Example

For symbol = '0', the output should be
solution(symbol) = true;
For symbol = '-', the output should be
solution(symbol) = false.
"""

def solution(symbol):
    return symbol.isdigit()

def solution(symbol):
    if 48<=ord(symbol)<=57:
        return(True)
    else:
        return(False)

def solution(s):
    return s.isdigit()

