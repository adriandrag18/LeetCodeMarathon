# title: Max Area of Island
# timestamp: 2025-01-06 18:41:37
# problemUrl: https://leetcode.com/problems/max-area-of-island/
# memory: 17.9 MB
# runtime: 17 ms

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        for k in range(m):
            for l in range(n):
                if grid[k][l] != 1:
                    continue
                area = 1
                q = [(k, l)]
                grid[k][l] = 2
                while q:
                    i, j = q.pop()
                    for i, j in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                            q.append((i, j))
                            area += 1
                            grid[i][j] = 2
                maxArea = max(maxArea, area)

        return maxArea