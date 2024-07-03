"""
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.
"""

# - -
l = lambda n:all([ int(i)%2==0 for i in str(n)])

def solution(n):
    return all([int(i)%2==0 for i in str(n)])

def solution(n):

    while n:
        if n % 2:
            return False
        n //= 10
    return True

def solution(n):
    return sum([int(i)%2 for i in str(n)])==0

def solution(n):
  for char in str(n):
    if int(char) % 2 != 0:
      return False
  return True


def solution(n):
    n1 = str(n)
    for i in n1:
        if int(i) % 2 != 0:
            return False
    else:
        return True


def solution(n):
    return all(int(d) % 2 == 0 for d in str(n))

def solution(n):
    s = str(n)
    for x in s:
        if int(x) % 2 != 0:
            return False
    return True


def solution(n):
    numString = str(n)
    for i in range(0, len(numString)):
        if (int(numString[i]) % 2 == 1):
            return False

    return True

def solution(n):
    n2 = str(n)
    a = [ x for x in n2 if int(x)%2 == 1]
    if a == []:
        return True
    else:
        return False

def solution(n):
    while n > 0:
        if n % 2 != 0: return False
        n //= 10
    return True


