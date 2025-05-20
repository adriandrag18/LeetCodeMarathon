# title: Missing Number
# timestamp: 2025-05-20 11:15:37
# problemUrl: https://leetcode.com/problems/missing-number/
# memory: 19 MB
# runtime: 0 ms

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for i in range(len(nums)):
            if i not in s:
                return i
        
        return len(nums)