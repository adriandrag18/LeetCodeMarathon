# title: Minimum Operations to Make Array Values Equal to K
# timestamp: 2024-12-07 16:35:48
# problemUrl: https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
# memory: 17.3 MB
# runtime: 60 ms

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        
        s = set(nums)
        if k == min(s):
            return len(set(nums)) - 1
        
        return len(set(nums))