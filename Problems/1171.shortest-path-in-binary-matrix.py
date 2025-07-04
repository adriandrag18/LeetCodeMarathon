# title: Shortest Path in Binary Matrix
# timestamp: 2025-06-21 17:11:07
# problemUrl: https://leetcode.com/problems/shortest-path-in-binary-matrix/
# memory: 19.8 MB
# runtime: 211 ms

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        if grid[-1][-1] == 1 or grid[0][0] == 1:
            return -1
        if n == 1 and m == 1:
            return 1
        
        seen = set([(0, 0)])
        queue = deque([(0, 0, 1)])
        while queue:
            x, y, dist = queue.popleft()
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n) or grid[nx][ny]:
                    continue
                if (nx, ny) in seen:
                    continue
                if (nx, ny) == (m - 1, n - 1):
                    return dist + 1
                seen.add((nx, ny))
                queue.append((nx, ny, dist + 1))
        
        return -1