# 5/1/2023

"""
Given an array of strings arr[]. You have to find the longest string which is lexicographically smallest and also all of its prefix strings are already present in the array.



Example 1:

Input: ab a abc abd
Output: abc
Explanation: We can see that length of the longest
string is 3. And there are two string "abc" and "abd"
of length 3. But for string "abc" , all of its prefix
"a" "ab" "abc" are present in the array. So the
output is "abc".
Example 2:

Input: ab a aa abd abc abda abdd abde abdab
Output: abdab
Explanation: We can see that each string is fulfilling
the condition. For each string, all of its prefix
are present in the array.And "abdab" is the longest
string among them. So the ouput is "abdab".


Your Task:
You don't need to read input or print anything. Your task is to complete the function longestString() which takes the array arr[] as input parameter and returns the longest string which is also lexicographically smallest.And if there is no such string return empty string.


Expected Time Complexity: O(NlogN)
Expected Space Complexity: O(N)



Constraints:
1 <= length of arr[] <= 103
1 <= arr[i].length <=30
"""

#User function Template for python3

class Solution():
    def longestString(self, arr, n):
        arr.sort()
        max=""
        dict={}
        dict[""]=1
        for i in range(n):
            if arr[i][:-1] in dict:
                dict[arr[i]]=1
                if len(max)<len(arr[i]):
                    max=arr[i]
        return max



#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends