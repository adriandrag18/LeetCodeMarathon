# title: Maximum Count of Positive Integer and Negative Integer
# timestamp: 2025-03-12 11:33:18
# problemUrl: https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= 0:
                r = m - 1
            else:
                l = m + 1
        neg = l

        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > 0:
                r = m - 1
            else:
                l = m + 1
        pos = len(nums) - l
        
        return max(neg, pos)