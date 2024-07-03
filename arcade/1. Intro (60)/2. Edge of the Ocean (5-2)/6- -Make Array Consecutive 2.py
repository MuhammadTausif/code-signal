"""
Ratiorg got `statues` of different sizes as a present from CodeMaster for his birthday,
each statue having an non-negative integer size. Since he likes to make things perfect, 
he wants to arrange them from smallest to largest so that each statue will be bigger than
 the previous one exactly by 1. He may need some additional statues to be able to accomplish that. 
 Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
"""

my_solution = lambda s: max(s) - min(s) - len(set(s)) + 1

def solution(statues):
    return len(set(list(range(min(statues), max(statues)))) - set(statues))

def solution(statues):
    return max(statues) - min(statues) - len(statues) + 1

def solution(statues):
    return sum([1 for i in range(min(statues), max(statues)) if i not in statues])

def solution(statues):
    return max(statues) - min(statues) - len(statues) + 1

def solution(statues):
    return max(statues) - min(statues) + 1 - len(statues)

def solution(statues):
    largest = max(statues)
    smallest = min(statues)
    nums = largest - smallest + 1 - len(statues)
    return nums

def solution(statues):
    list.sort(statues)
    return statues[-1] - statues[0] + 1 - len(statues)

def solution(statues):
   return len(set(statues) ^ set(range(min(statues), max(statues) + 1)))

def solution(statues):
    return max(statues) - min(statues) - len(statues) + 1