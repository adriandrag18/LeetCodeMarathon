# title: Search Insert Position
# timestamp: 2025-01-04 00:45:39
# problemUrl: https://leetcode.com/problems/search-insert-position/
# memory: 18.6 MB
# runtime: 0 ms

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        
        return l