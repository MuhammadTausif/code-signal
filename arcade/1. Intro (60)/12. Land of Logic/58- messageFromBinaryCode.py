"""
You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must be an encrypted message. After some thought, your first guess is that each consecutive 8 bits of the code stand for the character with the corresponding extended ASCII code.

Assuming that your hunch is correct, decode the message.

Example

For code = "010010000110010101101100011011000110111100100001", the output should be
solution(code) = "Hello!".

The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
Other letters can be obtained in the same manner.
"""

def solution(code):
    return "".join([chr(int(code[8*i:8*i+8],2)) for i in range(len(code)//8)])

def solution(c):
    return "".join([chr(int(c[i:i+8],2)) for i in range(0,len(c),8)])

def solution(code):
    ret = ""
    for i in range(0, len(code), 8):
        num = int(code[i:i + 8], 2)
        ret += chr(num)
    return ret

def solution(code):
    return int(code, 2).to_bytes((int(code, 2).bit_length() + 7) // 8, 'big').decode()

def solution(code):
    n = int(code, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def solution(code):
    return "".join([chr(int(c,2)) for c in [code[i:i+8] for i in range(0,len(code),8)]])

def solution(code):
    return ''.join(map(chr, [int(code[i : 8+i], 2) for i in range(0, len(code), 8)]))

def solution(code):
    ans=''
    for x in range(0, len(code)-7, 8):
        ans+=chr(int(code[x:x+8], 2))
    return ans