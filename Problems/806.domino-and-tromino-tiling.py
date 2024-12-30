# title: Domino and Tromino Tiling
# timestamp: 2024-12-30 16:47:53
# problemUrl: https://leetcode.com/problems/domino-and-tromino-tiling/
# memory: 17.9 MB
# runtime: 1 ms

class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 1, 2] + [0] * n
        mod = 10**9 + 7
        for i in range(2, n):
            dp[i + 1] = (2 * dp[i] + dp[i - 2]) % mod
        
        return dp[n]