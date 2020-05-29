"""
# Greedy-3

## Problem1 Queue Reconstruction by Height (https://leetcode.com/problems/queue-reconstruction-by-height/)

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

time- O(N^2)
space- 1
"""

class Solution:
    def reconstructQueue(self, people):
        people.sort(key = lambda x:(-x[0],x[1]))
        output=[]
        for i in people:
            output.insert(i[1], i)
        return output

rq = Solution()
print(rq.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))