# title: Maximum Amount of Money Robot Can Earn
# timestamp: 2025-01-12 06:03:11
# problemUrl: https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/
# memory: 85.5 MB
# runtime: 1883 ms

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [[[-10**6] * 3 for _ in range(n+1)] for _ in range(m+1)]
        dp[m-1][n] = [0] * 3
        dp[m][n-1] = [0] * 3

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                for k in range(3):
                    dp[i][j][k] = max(dp[i+1][j][k], dp[i][j+1][k]) + coins[i][j]
                if coins[i][j] < 0:
                    dp[i][j][0] = max([dp[i][j][0], dp[i+1][j][1], dp[i][j+1][1]])
                    dp[i][j][1] = max([dp[i][j][1], dp[i+1][j][2], dp[i][j+1][2]])
        
        return max(dp[0][0])