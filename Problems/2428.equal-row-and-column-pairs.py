# title: Equal Row and Column Pairs
# timestamp: 2024-12-30 12:01:11
# problemUrl: https://leetcode.com/problems/equal-row-and-column-pairs/
# memory: 22 MB
# runtime: 20 ms

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        map = {}
        for line in grid:
            map[tuple(line)] = map.get(tuple(line), 0) + 1
        
        res = 0
        for i in range(len(grid)):
            l = []
            for j in range(len(grid)):
                l.append(grid[j][i])
            res += map.get(tuple(l), 0)

        return res