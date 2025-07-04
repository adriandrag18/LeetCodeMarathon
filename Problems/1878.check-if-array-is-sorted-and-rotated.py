# title: Check if Array Is Sorted and Rotated
# timestamp: 2025-02-02 13:59:20
# problemUrl: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        
        miss = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                miss += 1
        
        return miss <= 1