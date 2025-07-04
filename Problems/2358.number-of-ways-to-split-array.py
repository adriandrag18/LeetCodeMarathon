# title: Number of Ways to Split Array
# timestamp: 2025-01-04 00:38:13
# problemUrl: https://leetcode.com/problems/number-of-ways-to-split-array/
# memory: 32.5 MB
# runtime: 40 ms

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res, partialSum, totalSum = 0, 0, sum(nums)
        for num in nums[:-1]:
            partialSum += num
            if totalSum <= 2 * partialSum:
                res += 1
        
        return res
