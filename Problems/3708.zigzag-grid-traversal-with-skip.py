# title: Zigzag Grid Traversal With Skip
# timestamp: 2025-01-12 04:35:35
# problemUrl: https://leetcode.com/problems/zigzag-grid-traversal-with-skip/
# memory: 18.1 MB
# runtime: 3 ms

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        i, j = 0, 0
        step = 1
        res = []
        while i < m:
            
            while 0 <= j < n:
                if (i + j) % 2 == 0:
                    res.append(grid[i][j])
                j += step
            j -= step
            step = -step
            i += 1

        return res