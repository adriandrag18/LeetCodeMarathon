# title: Maximum Difference Between Increasing Elements
# timestamp: 2025-06-16 15:23:15
# problemUrl: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        currMin = nums[0]
        res = 0
        for num in nums[1:]:
            res = max(res, num - currMin)
            currMin = min(currMin, num)
        
        return res if res else -1