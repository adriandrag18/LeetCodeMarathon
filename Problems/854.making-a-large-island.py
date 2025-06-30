# title: Making A Large Island
# timestamp: 2025-01-31 14:40:06
# problemUrl: https://leetcode.com/problems/making-a-large-island/
# memory: 27.3 MB
# runtime: 458 ms

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, color):
            count = 1
            queue = [(i, j)]
            grid[i][j] = color
            while queue:
                i, j = queue.pop()
                for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1):
                        continue
                    
                    queue.append((ni, nj))
                    grid[ni][nj] = color
                    count += 1
            
            map[color] = count
        
        map = {}
        no = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    no += 1
                    dfs(i, j, no + 1)
        
        # print(*grid, no, sep='\n')
        
        if no == 0:
            return 1
        
        res = max(map.values())
        # print(res)
        for i in range(n):
            for j in range(n):
                sum = 1
                seen = set()
                if grid[i][j] != 0:
                    continue

                for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    ni, nj = i + di, j + dj
                    # print(ni, nj, grid[ni][nj] if 0 <= ni < n and 0 <= nj < n else -1)
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1 and grid[ni][nj] not in seen:
                        sum += map[grid[ni][nj]]
                        seen.add(grid[ni][nj])

                res = max(res, sum)

        return res
