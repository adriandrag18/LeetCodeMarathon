# title: Minimum Cost to Make at Least One Valid Path in a Grid
# timestamp: 2025-01-18 22:33:46
# problemUrl: https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/
# memory: 18.9 MB
# runtime: 85 ms

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0
        
        queue = deque([(0, 0)])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            x, y = queue.popleft()
            for i, (dx, dy) in enumerate(directions): 
                nx, ny = x + dx, y + dy
                cost = 1 if grid[x][y] != i + 1 else 0
                
                if 0 <= nx < m and 0 <= ny < n and dp[x][y] + cost < dp[nx][ny]:
                    dp[nx][ny] = dp[x][y] + cost
                    if cost == 1:
                        queue.append((nx, ny))
                    else:
                        queue.appendleft((nx, ny))
        
        return dp[m - 1][n - 1]
