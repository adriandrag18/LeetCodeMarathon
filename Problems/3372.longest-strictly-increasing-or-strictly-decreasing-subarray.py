# title: Longest Strictly Increasing or Strictly Decreasing Subarray
# timestamp: 2025-02-03 16:43:52
# problemUrl: https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# memory: 18 MB
# runtime: 3 ms

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        res = 1
        currUp, currDown = 1, 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                currUp += 1
                res = max(res, currUp)
            else: 
                currUp = 1
            if nums[i] > nums[i + 1]:
                currDown += 1
                res = max(res, currDown)
            else:
                currDown = 1
            
            # print(i, nums[i + 1], currUp, currDown, res)

        return res