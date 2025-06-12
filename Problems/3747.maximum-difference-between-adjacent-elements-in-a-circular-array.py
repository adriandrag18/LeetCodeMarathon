# title: Maximum Difference Between Adjacent Elements in a Circular Array
# timestamp: 2025-06-12 10:53:56
# problemUrl: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/
# memory: 17.8 MB
# runtime: 3 ms

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            diff = nums[i] - nums[(i + 1) % n]
            res = max([res, diff, -diff])
        
        return res
