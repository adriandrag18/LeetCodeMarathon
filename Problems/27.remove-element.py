# title: Remove Element
# timestamp: 2025-01-04 01:26:31
# problemUrl: https://leetcode.com/problems/remove-element/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
                continue
            l += 1
        
        if nums[r] == val:
            r -= 1
        
        return r + 1
