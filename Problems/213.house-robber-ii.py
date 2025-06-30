# title: House Robber II
# timestamp: 2025-01-06 19:45:07
# problemUrl: https://leetcode.com/problems/house-robber-ii/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        prev, curr = nums[0], nums[0]

        for num in nums[2:n-1]:
            curr, prev = max(curr, prev + num), curr
        res = curr

        prev, curr = 0, nums[1]
        for num in nums[2:]:
            curr, prev = max(curr, prev + num), curr
            
        return max(res, curr)