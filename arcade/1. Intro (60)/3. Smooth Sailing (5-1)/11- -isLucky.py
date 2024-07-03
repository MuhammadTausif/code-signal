"""
Ticket numbers usually consist of an even number of digits.
 A ticket number is considered lucky if the sum of the 
 first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
"""
# - -
l = lambda n: sum(list(map(int,str(n)[:len(list(map(int, str(n))))//2]))) == sum(list(map(int,str(n)[len(list(map(int, str(n))))//2:])))

my_solution = lambda n: 0

def solution(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))


def solution(n):
    s = [int(x) for x in str(n)]
    l = int(len(s) / 2)
    return sum(s[:l]) == sum(s[l:])

def solution(n):
    n = list(map(int, str(n)))
    l = len(n) // 2
    return sum(n[:l]) == sum(n[l:])

def solution(n):
    return sum([int(i) for i in str(n)[:len(str(n))//2]]) == sum([int(i) for i in str(n)[len(str(n))//2:len(str(n))]])


def solution(n):
    # Convert n to a list of chars
    n = list(str(n))
    # Convert n to a list of ints
    n = list(map(int, n))
    # Grab the halfway point of the list
    nLen = int(len(n) / 2)
    # Divide the list into the halves to compare the sum
    firstHalf, secondHalf = n[0:nLen], n[nLen:]

    return sum(firstHalf) == sum(secondHalf)

def solution(n):
    s1 = 0
    for i in range(len(str(n))//2):
        s1 += n%10
        n //= 10
    for i in range(len(str(n))):
        s1 -= n%10
        n //= 10
    return s1 == 0

def solution(n):
    x=str(n)
    l=len(x)
    if (l%2==0):
        half=int(l/2)
        fh=x[0:half]
        sh=x[half:l]
        fh_s=0
        for i in fh:
            fh_s+=int(i)
        sh_s=0
        for i in sh:
            sh_s+=int(i)
        if fh_s==sh_s:
            return (1==1)
        else:
            return (1==0)
    else:
        return (1==0)

def solution(n):
    strN = [int(x) for x in str(n)]
    return sum(strN[0:len(strN)//2]) == sum(strN[len(strN)//2:])

def solution(n):
    n = [int(x) for x in str(n)]
    m = len(n)//2
    return sum(n[:m]) == sum(n[m:])










