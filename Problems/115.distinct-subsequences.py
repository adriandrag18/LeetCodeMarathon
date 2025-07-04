# title: Distinct Subsequences
# timestamp: 2025-06-30 10:58:55
# problemUrl: https://leetcode.com/problems/distinct-subsequences/
# memory: 74.2 MB
# runtime: 294 ms

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0] = [1] * (n + 1)
        for i in range(1, m + 1):
            for j in range(i, n + 1):
                dp[i][j] = dp[i][j-1]
                if s[j-1] == t[i-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        return dp[-1][-1]

