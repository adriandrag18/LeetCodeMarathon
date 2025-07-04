# title: Monotonic Array
# timestamp: 2025-06-12 20:25:36
# problemUrl: https://leetcode.com/problems/monotonic-array/
# memory: 29 MB
# runtime: 27 ms

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec, inc = True, True
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                dec = False
                if not inc:
                    return False
            if nums[i - 1] > nums[i]:
                inc = False
                if not dec:
                    return False
        
        return True