# title: Maximum Product Subarray
# timestamp: 2025-05-24 13:11:03
# problemUrl: https://leetcode.com/problems/maximum-product-subarray/
# memory: 18.4 MB
# runtime: 9 ms

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # if n == 1:
        #     return nums[0]
            
        # dp = [0] * n
        # res = dp[0] = nums[0]
        # lastZero = -1
        # for i in range(1, n):
        #     dp[i] = nums[i]
        #     res = max(res, dp[i])
        #     if nums[i] == 0:
        #         lastZero = i
        #     for j in range(lastZero + 1, i):
        #         dp[j] *= nums[i]
        #         res = max(res, dp[j])

        res = minProd = maxProd = nums[0]
        for i in range(1, n):
            tmp = minProd * nums[i]
            minProd = min(tmp, maxProd * nums[i], nums[i])
            maxProd = max(tmp, maxProd * nums[i], nums[i])
            res = max(res, maxProd)
    
        return res
