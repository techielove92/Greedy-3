"""
## Problem2 Partition Labels (https://leetcode.com/problems/partition-labels/)

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"

Output: [9,7,8]

Explanation:

The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

S will have length in range [1, 500].

S will consist of lowercase letters ('a' to 'z') only.

time - O(n)
space- constant , O(26)
"""
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic={}
        for i in range(len(S)):
            dic[S[i]] = i

        start=0
        end=0
        output=[]
        for i in range(len(S)):
            end = max(end,dic[S[i]])
            end +=1
            if i == end:
                output.append(i)
                start=end+1
        return output