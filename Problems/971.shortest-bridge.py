# title: Shortest Bridge
# timestamp: 2025-06-11 19:45:27
# problemUrl: https://leetcode.com/problems/shortest-bridge/
# memory: 21.4 MB
# runtime: 99 ms

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            queue.append((i, j))
            for ni, nj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                    dfs(ni, nj)
        
        queue = deque()
        n = len(grid)
        grid = [[el if el else float('inf') for el in line] for line in grid]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    break
            else:
                continue
            break
        # print(*grid, sep='\n')
        while queue:
            i, j = queue.popleft()
            for ni, nj in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj] == float('inf'):
                        grid[ni][nj] = grid[i][j] - 1
                        queue.append((ni, nj))
                    if grid[ni][nj] == 1:
                        return -grid[i][j]
            
            # print(*grid, sep='\n')
                        
        return -100
