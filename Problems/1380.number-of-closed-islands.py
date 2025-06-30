# title: Number of Closed Islands
# timestamp: 2025-06-13 23:25:33
# problemUrl: https://leetcode.com/problems/number-of-closed-islands/
# memory: 18.5 MB
# runtime: 11 ms

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            # mark the cell so we dont check it again
            grid[i][j] = 2
            # go through its neighbours and check if there are land
            for ni, nj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                    dfs(ni, nj)

        # dfs from every cell on the edges
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n-1] == 0:
                dfs(i, n - 1)
        
        for j in range(1, n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m-1][j] == 0: 
                dfs(m - 1, j)
        
        # dfs from every other cell and keep count of the islend
        count = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        
        return count