# title: Find Minimum in Rotated Sorted Array
# timestamp: 2024-12-12 18:15:42
# problemUrl: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# memory: 17.6 MB
# runtime: 0 ms

class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = nums[-1]
        if nums[0] < last:
            return nums[0]

        l, r = 0, len(nums) - 2
        while l <= r:
            m = (l + r) // 2
            if nums[m] > last:
                l = m + 1
                continue
            r = m - 1
        
        return nums[r + 1]