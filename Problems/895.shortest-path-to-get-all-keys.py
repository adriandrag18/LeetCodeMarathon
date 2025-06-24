# title: Shortest Path to Get All Keys
# timestamp: 2025-06-24 16:24:06
# problemUrl: https://leetcode.com/problems/shortest-path-to-get-all-keys/
# memory: 23.9 MB
# runtime: 275 ms

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        start = (-1, -1)
        keyCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif grid[i][j].isalpha() and grid[i][j].islower():
                    keyCount += 1
        
        seen = set([(*start, '')])
        queue = deque([(*start, 0, '')])
        while queue:
            i, j, dist, keys = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if not (0 <= ni < m and 0 <= nj < n) or grid[ni][nj] == '#':
                    continue
                if grid[ni][nj].isalpha() and grid[ni][nj].isupper() and grid[ni][nj].lower() not in keys:
                        continue
                
                newKeys = [k for k in keys]
                if grid[ni][nj].isalpha() and grid[ni][nj].islower() and grid[ni][nj] not in newKeys:
                    if len(newKeys) == keyCount - 1:
                        return dist + 1
                    newKeys.insert(bisect_left(newKeys, grid[ni][nj]), grid[ni][nj])
                
                if (ni, nj, ''.join(newKeys)) in seen:
                    continue

                queue.append((ni, nj, dist + 1, ''.join(newKeys)))
                seen.add(((ni, nj, ''.join(newKeys))))
        
        return -1
                
                
                
