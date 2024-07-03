"""
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
solution(yourLeft, yourRight, friendsLeft, friendsRight) = false.
"""

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return sorted([yourLeft,yourRight])==sorted([friendsLeft,friendsRight])

def solution(ul, ur, fl, fr):
    return max(ul, ur) == max(fl, fr) and min(ul, ur) == min(fl, fr)

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return (set([yourLeft, yourRight]) == set([friendsLeft, friendsRight]))

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return max(yourLeft, yourRight)==max(friendsLeft, friendsRight) and min(yourLeft, yourRight)==min(friendsLeft, friendsRight)


def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return (set([yourLeft, yourRight]) == set([friendsLeft, friendsRight]))


def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return max(yourLeft, yourRight)==max(friendsLeft, friendsRight) and min(yourLeft, yourRight)==min(friendsLeft, friendsRight)

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return [yourLeft,yourRight] == [friendsLeft,friendsRight] or [yourLeft,yourRight] == [friendsRight,friendsLeft]

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and min(yourLeft, yourRight) == min(friendsLeft, friendsRight)


def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    return max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and min(yourLeft, yourRight) == min(friendsLeft,
                                                                                                          friendsRight)

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    if max(yourLeft,yourRight) == max(friendsLeft,friendsRight) and min(yourLeft,yourRight) == min(friendsLeft,friendsRight):
        return True
    else:
        return False


def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    sum_a = yourLeft + yourRight
    sum_b = friendsLeft + friendsRight
    if max(yourLeft, yourRight) == max(friendsLeft, friendsRight):
        if sum_a == sum_b:
            return True

    return False




