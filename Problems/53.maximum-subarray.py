# title: Maximum Subarray
# timestamp: 2025-06-08 01:35:40
# problemUrl: https://leetcode.com/problems/maximum-subarray/
# memory: 32.6 MB
# runtime: 60 ms

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _max, curr = nums[0], nums[0]
        for num in nums[1:]:
            if curr < 0:
                curr = 0
            curr += num
            _max = max(_max, curr)
        
        return _max