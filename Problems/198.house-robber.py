# title: House Robber
# timestamp: 2025-01-06 19:35:58
# problemUrl: https://leetcode.com/problems/house-robber/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        prev, curr = nums[0], max(nums[:2])

        for num in nums[2:]:
            curr, prev = max(curr, prev + num), curr
        
        return curr