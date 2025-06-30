# title: Find First and Last Position of Element in Sorted Array
# timestamp: 2025-01-13 19:18:16
# problemUrl: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# memory: 19 MB
# runtime: 0 ms

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        found = False
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
                continue
            if nums[m] == target:
                found = True
            r = m - 1
        
        if not found:
            return [-1, -1]
        
        first = l

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
                continue
            r = m - 1
        
        last = r
        return [first, last]