"""
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
solution(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
solution(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.
"""


def solution(inputArray):
    # FIRST
    # Note that the task is equivalent to finding a Hamiltonian path in the graph where the nodes are our strings
    # and there is an edge where the distance between two strings is one.
    # Hamiltonian path is NP-complete but this possibly is not because we are looking at a specific subset of all graphs.
    # Intuitively: incomplete hypercubes but I have not constructed a proof.
    # I have come to expect that the most upvoted solution to these is a fancy oneliner by someone who just 'gets' it.
    # So I assume my solution building on that intuition is too complicated

    # SECOND
    # Note that in  ["aaaa", "aaab", "aabb", "abbb", "abab", "baab"] every vertex except the first and the last have
    # two neighbours and yet there is no solution. None of the sample tests is of that kind.
    # This means that the sample tests pass with a way to easy solution.

    # THIRD
    # Note that the hypercube can be broken into two or more parts like so:
    # ["ccaa", "ccab", "ccba", "ccbb", "ddaa", "ddab", "ddba", "ddbb"]
    # This test case will also fail with the overly simple solution which all the other samples pass.

    # FOURTH
    # https://app.codesignal.com/forum/btzBAiv9irK3yc4RT

    # FIFTH
    # Now that I have actually seen the most upvoted solution it uses permutations (i. e. brute force).
    # I am suprised that this is fast enough.
    # It is pretty obvious that my approach on average considers far less options than the brute force approach
    # but it burns more time on every permutation to find shortcuts
    # so in the end I think my approach is faster for larger N

    def recursion(N, n, k, adjaceny, adj, tab):
        if n == (N - 1):
            return n

        # Keep tab of all vertices already used as a starting vertice.
        # This solution starts over with the last vertice of a dead end as the start.
        # Empirically it works pretty well on the tests.
        # What this means is that if the graph broken into parts,
        # starting vertices not reachable from the 0-vertex are not even considered.
        if n == 0:
            tab = tab | set([k])

        # Remove k from all further considerations
        adj2 = [row[:] for row in adj]
        for j in range(N):
            adj2[j][k] = False
            adj2[k][j] = False

        max = n
        for j in range(N):
            if adj[k][j]:
                # Obviously we want to search depth first so that we can stop if we complete a path.
                u = recursion(N, n + 1, j, adjaceny, adj2, tab)
                if u == (N - 1):
                    return u

                # Failing to find a solution below j, what about solutions that start with j?
                if j not in tab:
                    v = recursion(N, 0, j, adjaceny, adjaceny, tab)
                    if v == (N - 1):
                        return v
                    if v > max:
                        max = v
                if u > max:
                    max = u
        # This is just cosmetics.
        return max

    N = len(inputArray)

    adjaceny = [[False] * N for i in range(N)]

    for j in range(N - 1):
        for i in range(j + 1, N):
            hamming = sum(u != v for u, v in zip(inputArray[i], inputArray[j]))
            adjaceny[i][j] = (hamming == 1)
            adjaceny[j][i] = (hamming == 1)

    # At most two vertices can have degree one. The first and the last in the sequence.
    # All other vertices need to have degree > 1
    # We can use that property to optimise
    degOne = set()
    for i in range(N):
        s = sum(adjaceny[i])
        if s == 0:
            return False
        if s == 1:
            degOne = degOne | set([i])
    if len(degOne) > 2:
        return False

    tab = set() if len(degOne) == 0 else set(range(N)) - degOne

    p = recursion(N, 0, 0, adjaceny, adjaceny, tab)

    return (N - 1) == p


from itertools import permutations

def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def solution(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False


from itertools import permutations as p
def solution(inputArray):
    for ia in p(inputArray):
        c = 0
        for i in range(len(ia) - 1):
            for j in range(len(ia[i])):
                if ia[i][j] != ia[i+1][j]: c += 1
            if ia[i] == ia[i+1]: c += 10
        if c == len(ia) - 1: return True
    return False

def solution(inputArray):
    for startIndex in range(len(inputArray)):
        if isChainPossible(startIndex, inputArray):
            return True
    return False

def isChainPossible(startIndex, array):
    if len(array) == 1:
        return True
    newArray = array[:startIndex] + array[(1 + startIndex):]
    for i in range(len(newArray)):
        if differsByOne(array[startIndex], newArray[i]) and \
           isChainPossible(i, newArray):
            return True
    return False

def differsByOne(s1, s2):
    if len(s1) != len(s2):
        return False
    differentChars = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            differentChars += 1
    return differentChars == 1

# recursive DFS
# could be done as iterative DFS

from itertools import permutations


def solution(inputArray):
    def diffBy1(st1, st2):
        return sum(a != b for a, b in zip(st1, st2)) == 1

    def goodList(lst):
        return all(diffBy1(lst[i], lst[i + 1]) for i in range(len(lst) - 1))

    return any(map(goodList, permutations(inputArray)))


import numpy as np


def node_swap(graph, n1, n2):
    graph[[n1, n2]] = graph[[n2, n1]]
    graph[:, [n1, n2]] = graph[:, [n2, n1]]
    return graph


def dfs(graph):
    if len(graph) < 2:
        return True
    elif sum(graph[0]) == 0:
        return False
    print(graph)
    for i in range(1, len(graph)):
        if graph[0][i] == 1:
            graph = node_swap(graph, 1, i)
            if dfs(graph[1:, 1:]): return True
            graph = node_swap(graph, i, 1)
    return False


def solution(s_in):
    # build a map of possible adjacencies:
    neighbors = np.zeros((len(s_in), len(s_in)))
    for i, s in enumerate(s_in):
        for j in range(i + 1, len(s_in)):
            diff = 0
            for k, c in enumerate(s):
                if c != s_in[j][k]: diff += 1
            if diff == 1:
                neighbors[i][j] = 1
                neighbors[j][i] = 1
    for i in range(len(neighbors)):
        if dfs(node_swap(neighbors, 0, i)): return True
    return False

import itertools

def solution(inputArray):
    arrs = list(itertools.permutations(inputArray))
    for entry in arrs:
        if inOrder(entry):
            return True
    return False

def inOrder(a):
    for i in range(0,len(a)-1):
        if (not differByOne(a[i],a[i+1])):
            return False
    return True

def differByOne(s1,s2):
    check = False
    for i in range(0, len(s1)):
        if (check and s1[i] != s2[i]):
            return False
        if (s1[i] != s2[i]):
            check = True
    return check


def match(s1, s2):
    found_diff = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if found_diff:
                return False
            else:
                found_diff = True
    return found_diff


def is_solved(a):
    for idx in range(len(a)-1):
        if not match(a[idx], a[idx+1]):
            return False
    return True


def is_solvable(a, start, end):
    if is_solved(a):
        return True
    else:
        for i in range(start, end):
            a[start], a[i] = a[i], a[start]
            found = is_solvable(a, start+1, end)
            a[i], a[start] = a[start], a[i]
            if found:
                return True


def solution(a):
    if is_solvable(a, 0, len(a)):
        return True
    else:
        return False


def difference(stringA, stringB):
    result = 0
    for pair in zip(stringA, stringB):
        result += pair[0] != pair[1]
    return result


def calculateStringAdjacency(strings):
    stringCount = len(strings)

    adjacency = [[False] * stringCount for i in range(stringCount)]

    for i in range(stringCount - 1):
        for j in range(i + 1, stringCount):
            adjacent = difference(strings[i], strings[j]) == 1
            adjacency[i][j] = adjacent
            adjacency[j][i] = adjacent

    return adjacency


def hamiltonianPathExists(adjacency, unusedVertces, pathEnd):
    for index, vertex in enumerate(unusedVertces):
        if adjacency[vertex][pathEnd]:
            if len(unusedVertces) == 1 or hamiltonianPathExists(adjacency,
                                                                unusedVertces[:index] + unusedVertces[index + 1:],
                                                                vertex):
                return True
    return False


def solution(inputArray):
    adjacency = calculateStringAdjacency(inputArray)
    unusedVertces = [vertex for vertex in range(len(inputArray))]

    for index, vertex in enumerate(unusedVertces):
        if hamiltonianPathExists(adjacency, unusedVertces[:index] + unusedVertces[index + 1:], vertex):
            return True

    return False

