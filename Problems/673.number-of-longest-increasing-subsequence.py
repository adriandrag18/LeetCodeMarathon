# title: Number of Longest Increasing Subsequence
# timestamp: 2025-06-21 20:53:24
# problemUrl: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
# memory: 18 MB
# runtime: 442 ms

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        nums = [-float('inf')] + nums
        n = len(nums)
        dp = [1] * n
        counts = [1] * n

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    if dp[i] == dp[j] + 1:
                        counts[i] += counts[j]
                    elif dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        counts[i] = counts[j]
                
        return counts[0]
