# title: First Missing Positive
# timestamp: 2025-06-09 12:48:33
# problemUrl: https://leetcode.com/problems/first-missing-positive/
# memory: 28.9 MB
# runtime: 52 ms

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            j = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1

        for i in range(n):
            if i != nums[i] - 1:
                return i + 1
        
        return n + 1