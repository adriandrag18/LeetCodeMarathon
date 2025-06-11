# title: Zero Array Transformation I
# timestamp: 2025-05-20 10:09:16
# problemUrl: https://leetcode.com/problems/zero-array-transformation-i/
# memory: 55.2 MB
# runtime: 75 ms

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        freq = [0] * (len(nums) + 1)
        for q in queries:
            freq[q[0]] += 1
            freq[q[1]+1] -= 1
        
        pSum = 0
        
        for i, n in enumerate(nums):
            pSum += freq[i]
            if pSum < n:
                return False
        
        return True