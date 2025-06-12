# title: Number of Enclaves
# timestamp: 2025-06-12 13:01:41
# problemUrl: https://leetcode.com/problems/number-of-enclaves/
# memory: 53.6 MB
# runtime: 87 ms

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j, k):
            grid[i][j] = 0
            for ni, nj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    dfs(ni, nj, k)
        
        for i in range(m):
            if grid[i][0] == 1:
                dfs(i, 0, 0)
            if grid[i][n-1] == 1:
                dfs(i, n-1, 0)
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j, 0)
            if grid[m-1][j] == 1:
                dfs(m-1, j, 0)
                
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                count += grid[i][j]
        
        return count