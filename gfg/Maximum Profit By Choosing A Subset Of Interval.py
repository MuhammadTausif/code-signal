# 4/1/2023

from typing import List


def search(arr, ele):
    l = 0
    ans = len(arr)
    h = len(arr) - 1
    while l <= h:
        mid = (l + h) // 2
        if arr[mid][0] < ele:
            l = mid + 1
        else:
            h = mid - 1
            ans = min(ans, mid)
    return ans


class Solution:
    def maximum_profit(self, n: int, intervals: List[List[int]]) -> int:
        # code here
        # [[1, 2, 3], [2, 4, 4], [1, 5, 7]]
        intervals.sort(key=lambda x: x[0])
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            ind = search(intervals, intervals[i][1])
            if ind >= n:
                dp[i] = intervals[i][2]
            else:
                dp[i] = (intervals[i][2] + dp[ind])

            if i != n - 1:
                dp[i] = max(dp[i], dp[i + 1])
        return dp[0]


# {
# Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        intervals = IntMatrix().Input(n, 3)

        obj = Solution()
        res = obj.maximum_profit(n, intervals)

        print(res)

# } Driver Code Ends

# from typing import List
#
#
# class Solution:
#     def maximum_profit(self, n: int, intervals: List[List[int]]) -> int:
#         intervals.sort(key=lambda x: (x[1], x[0]))
#         M = intervals[-1][1]
#         dp = [0] * (M + 1)
#         for i in range(n):
#             s, e, p = intervals[i]
#             if p + dp[s] > dp[e]:
#                 dp[e] = p + dp[s]
#             if i < n - 1:
#                 _, en, _ = intervals[i + 1]
#                 for j in range(e + 1, en + 1):
#                     dp[j] = dp[e]
#         return dp[M]
#
#
# class Solution:
#     def maximum_profit(self, n : int, intervals : List[List[int]]) -> int:
#         intervals.sort()
#         S = [s for (s, e, p) in intervals]
#         dp = [0] * (n + 1)
#         for k in reversed(range(n)):
#             temp = bisect_left(S, intervals[k][1])
#             dp[k] = max(intervals[k][2] + dp[temp], dp[k+1])
#         return dp[0]