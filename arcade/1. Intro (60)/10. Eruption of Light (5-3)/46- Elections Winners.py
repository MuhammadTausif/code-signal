"""
Elections are in progress!

Given an array of the numbers of votes given to each of the candidates so far,
 and an integer k equal to the number of voters who haven't cast their vote yet,
 find the number of candidates who still have a chance to win the election.

The winner of the election must secure strictly more votes than any other candidate.
 If two or more candidates receive the same (maximum) number of votes,
 assume there is no winner at all.

Example

For votes = [2, 3, 5, 2] and k = 3, the output should be
solution(votes, k) = 2.

The first candidate got 2 votes. Even if all of the remaining 3 candidates vote for him, he will still have only 5 votes, i.e. the same number as the third candidate, so there will be no winner.
The second candidate can win if all the remaining candidates vote for him (3 + 3 = 6 > 5).
The third candidate can win even if none of the remaining candidates vote for him. For example, if each of the remaining voters cast their votes for each of his opponents, he will still be the winner (the votes array will thus be [3, 4, 5, 3]).
The last candidate can't win no matter what (for the same reason as the first candidate).
Thus, only 2 candidates can win (the second and the third), which is the answer.
"""

def solution(v, k):
    c, mv = 0, max(v)
    if k==0 and v.count(mv)==1: c=1
    for i in v:
        if i+k>mv: c+=1
    return c

def solution(votes, k):
    m = max(votes)
    pv = [x for x in votes if x+k > m]
    return 1 if k==0 and votes.count(m) == 1 else len(pv)

def solution(votes, k):
    SortedV = sorted(votes, reverse=True)
    if k == 0:
        return int(SortedV[0] != SortedV[1])
    else:
        return sum(v + k > SortedV[0] for v in SortedV)

def solution(votes, k):
    x = max(votes)
    cnt = votes.count(x)
    ret = 0
    for i in votes:
        if i + k > x or (i == x and cnt == 1):
            ret += 1
    return ret

import numpy
def solution(votes, k):
    return (sum(numpy.array(votes) + k > max(votes))) + (k==0 and sum(numpy.array(votes)==max(votes))==1)