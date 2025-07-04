# title: Longest Increasing Path in a Matrix
# timestamp: 2025-06-02 15:30:23
# problemUrl: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# memory: 20.5 MB
# runtime: 120 ms

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        def solve(prev, i, j):
            if not (0 <= i < n) or not (0 <= j < m) or prev >= matrix[i][j]:
                return 0
            
            if dp[i][j]: return dp[i][j]
            
            dp[i][j] = 1 + max([
                solve(matrix[i][j], i - 1, j), 
                solve(matrix[i][j], i, j - 1), 
                solve(matrix[i][j], i, j + 1), 
                solve(matrix[i][j], i + 1, j),
            ])
            return dp[i][j]
        
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res, solve(-1, i, j))
        
        return res