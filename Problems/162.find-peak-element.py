# title: Find Peak Element
# timestamp: 2024-12-30 16:20:11
# problemUrl: https://leetcode.com/problems/find-peak-element/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                r = m
                continue
            l = m + 1
        
        return r