# title: Find Minimum in Rotated Sorted Array II
# timestamp: 2025-06-24 00:22:45
# problemUrl: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# memory: 18.1 MB
# runtime: 0 ms

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] > nums[m]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r -= 1
            
        return nums[l]