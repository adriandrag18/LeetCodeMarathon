# title: Combination Sum IV
# timestamp: 2025-06-11 14:08:02
# problemUrl: https://leetcode.com/problems/combination-sum-iv/
# memory: 17.7 MB
# runtime: 50 ms

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
            # print(dp)
        return dp[target]