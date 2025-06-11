# title: Edit Distance
# timestamp: 2025-01-06 12:10:18
# problemUrl: https://leetcode.com/problems/edit-distance/
# memory: 19.8 MB
# runtime: 23 ms

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        dp[0] = list(range(n + 1))
        for i in range(m + 1):
            dp[i][0] = i
        
        # Bottom up in 123ms (5x slower the top down)
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         dp[i][j] = dp[i-1][j-1] if word1[j-1] == word2[i-1] else 1 + min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]])
        
        def helper(i, j, dp):
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[j-1] == word2[i-1]:
                dp[i][j] = helper(i - 1, j - 1, dp)
                return dp[i][j]
            
            delete = helper(i - 1, j, dp)
            insert = helper(i, j - 1, dp)
            replace = helper(i - 1, j - 1, dp)
            dp[i][j] = 1 + min([delete, insert, replace])
            return dp[i][j] 

        helper(m, n, dp)
        return dp[m][n]