"""
Consider integer numbers from 0 to n - 1 written down 
 along the circle in such a way that the distance between
 any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written
 in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.


"""

def solution(n, firstNumber):
    return (firstNumber + n/2)%n

def solution(n, f):
    return f-n/2 if (f-n/2)>=0 else (f-n/2)+n

def solution(n, firstNumber):
    return (firstNumber+n//2)%n

solution=lambda n,f:[i%n for i in range(f+n//2+1)][::-1][0]

def solution(n, firstNumber):

    if int(n/2) > firstNumber:
        return int(n/2)+firstNumber
    else:
        return firstNumber-int(n/2)

def solution(n, firstNumber): return (firstNumber+n//2)%n

def solution(n, firstNumber):
    if firstNumber < n/2:
        return firstNumber + n/2
    else:
        return firstNumber - n/2



def solution(n, firstNumber):
    if firstNumber+(n/2)>=n:
        return firstNumber-(n/2)
    else:
        return firstNumber+(n/2)

def solution(n, firstNumber):
    return(n/2 +firstNumber if n/2 +firstNumber <= (n-1) else n/2+firstNumber -n )


def solution(n, firstNumber):
    # even is guaranteed for n

    numToJump = n / 2

    result = firstNumber + numToJump

    if result >= n:
        result -= n

    return result

