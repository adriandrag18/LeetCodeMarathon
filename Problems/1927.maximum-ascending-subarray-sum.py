# title: Maximum Ascending Subarray Sum
# timestamp: 2025-02-04 13:08:17
# problemUrl: https://leetcode.com/problems/maximum-ascending-subarray-sum/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum = res = old = nums[0]
        for num in nums[1:]:
            if old < num:
                sum += num
            else:
                sum = num
            res = max(res, sum)
            old = num

        return res