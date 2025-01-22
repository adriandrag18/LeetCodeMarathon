# title: Map of Highest Peak
# timestamp: 2025-01-22 15:42:32
# problemUrl: https://leetcode.com/problems/map-of-highest-peak/
# memory: 85.2 MB
# runtime: 870 ms

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def getNeighbers(x, y):
            neighbers = []
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and map[nx][ny] == -10**9:
                    neighbers.append((nx, ny))
            return neighbers


        m, n = len(isWater), len(isWater[0])
        water = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    water.append((i, j))
        
        map = [[-10**9] * n for _ in range(m)]
        for x, y in water:
            map[x][y] = 0

        queue = deque([(x, y, 0) for x, y in water])
        while queue:
            x, y, lvl = queue.popleft()
            for nx, ny in getNeighbers(x, y):
                map[nx][ny] = lvl + 1
                queue.append((nx, ny, lvl + 1))
        
        return map
