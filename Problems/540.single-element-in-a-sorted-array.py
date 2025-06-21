# title: Single Element in a Sorted Array
# timestamp: 2025-06-21 16:45:11
# problemUrl: https://leetcode.com/problems/single-element-in-a-sorted-array/
# memory: 24.9 MB
# runtime: 0 ms

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if (m == 0 or nums[m-1] != nums[m]) and (m == n - 1 or nums[m] != nums[m+1]):
                return nums[m]
            if m & 1 == 0 and (m == n - 1 or nums[m] != nums[m+1]):
                r = m - 1
            elif m & 1 and nums[m] != nums[m-1]:
                r = m - 1
            else:
                l = m + 1
        
        return nums[l]