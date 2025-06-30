# title: Maximal Square
# timestamp: 2025-06-15 15:23:10
# problemUrl: https://leetcode.com/problems/maximal-square/
# memory: 32.9 MB
# runtime: 135 ms

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix[0]), len(matrix)
        dp = [[1 if el == '1' else 0 for el in line] for line in matrix]

        res = max(dp[-1] + [dp[i][-1] for i in range(m)])
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if not dp[i][j]:
                    continue
                
                l = min(dp[i][j+1], dp[i+1][j])
                dp[i][j] = l + (1 if dp[i + l][j + l] else 0)
                
                res = max(res, dp[i][j])

        return res ** 2
