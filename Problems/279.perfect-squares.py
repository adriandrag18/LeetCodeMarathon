# title: Perfect Squares
# timestamp: 2025-06-04 17:07:42
# problemUrl: https://leetcode.com/problems/perfect-squares/
# memory: 18.2 MB
# runtime: 79 ms

dp = [float('inf')] * 10001
class Solution:
    def numSquares(self, n: int) -> int:
        if dp[0] == float('inf'):
            for i in range(101):
                ps = i ** 2
                dp[ps] = 1
                for j in range(10001 - ps):
                    dp[ps + j] = min(dp[ps + j], dp[j] + 1)
        
        return dp[n]