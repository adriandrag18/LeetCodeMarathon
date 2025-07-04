# title: Minimum Size Subarray Sum
# timestamp: 2025-06-15 19:44:05
# problemUrl: https://leetcode.com/problems/minimum-size-subarray-sum/
# memory: 28.3 MB
# runtime: 6 ms

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        curr = 0
        l = 0
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                curr -= nums[l]
                res = min(res, r - l + 1)
                l += 1
                if l > r:
                    return 1
        
        return res if res != float('inf') else 0
