# title: Number of Islands
# timestamp: 2025-01-06 18:39:20
# problemUrl: https://leetcode.com/problems/number-of-islands/
# memory: 19.9 MB
# runtime: 241 ms

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        for k in range(m):
            for l in range(n):
                if grid[k][l] != '1':
                    continue
                q = [(k, l)]
                grid[k][l] = '2'
                count += 1
                while q:
                    i, j = q.pop()
                    for i, j in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                        if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                            q.append((i, j))
                            grid[i][j] = '2'
        return count