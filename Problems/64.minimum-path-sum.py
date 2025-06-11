# title: Minimum Path Sum
# timestamp: 2025-06-05 12:48:54
# problemUrl: https://leetcode.com/problems/minimum-path-sum/
# memory: 20.2 MB
# runtime: 10 ms

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[float('inf')] * (m + 1)for _ in range(n + 1)]
        dp[1][0] = dp[0][1] = 0

        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])
        
        # print(*dp, sep='\n')

        return dp[-1][-1]
