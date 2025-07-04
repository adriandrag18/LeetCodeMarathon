# title: Count Unguarded Cells in the Grid
# timestamp: 2024-11-21 10:50:02
# problemUrl: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
# memory: 38.4 MB
# runtime: 258 ms

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        res = 0
        grid = [[0] * n for _ in range(m)]

        for i, j in walls:
            grid[i][j] = 1
        for i, j in guards:
            # print(i, j)
            grid[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    k = 1
                    while i >= k and grid[i-k][j] not in [1, 2]:
                        grid[i-k][j] = 3
                        k += 1
                    k = 1
                    while j >= k and grid[i][j-k] not in [1, 2]:
                        grid[i][j-k] = 3
                        k += 1
                    k = 1
                    while j < n - k and grid[i][j+k] not in [1, 2]:
                        grid[i][j+k] = 3
                        k += 1
                    k = 1
                    while i < m - k and grid[i+k][j] not in [1, 2]:
                        grid[i+k][j] = 3
                        k += 1
        
        # print(*grid, sep='\n')
        res = sum([line.count(0) for line in grid])

        return res
        