# title: Unique Paths II
# timestamp: 2025-06-12 12:39:33
# problemUrl: https://leetcode.com/problems/unique-paths-ii/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-el for el in line] for line in obstacleGrid]
        if dp[0][0] == -1 or dp[-1][-1] == -1:
            return 0
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j]:
                    continue
                dp[i][j] = (dp[i - 1][j] if 0 < i and dp[i - 1][j] != -1 else 0) + (dp[i][j - 1] if 0 < j and dp[i][j - 1] != -1 else 0)

        return dp[-1][-1]