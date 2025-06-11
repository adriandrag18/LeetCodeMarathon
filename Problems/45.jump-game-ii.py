# title: Jump Game II
# timestamp: 2025-01-07 22:52:03
# problemUrl: https://leetcode.com/problems/jump-game-ii/
# memory: 18.7 MB
# runtime: 360 ms

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10**9] * (n - 1) + [0]
        for i in range(n-2, -1, -1):
            # print(i, nums[i], dp[i+1:min(i + nums[i] + 1, n)])
            if nums[i] == 0:
                continue
            dp[i] = 1 + min(dp[i+1:min(i + nums[i] + 1, n)])
        # print(dp)
        return dp[0] if dp[0] != 10**9 else -1
