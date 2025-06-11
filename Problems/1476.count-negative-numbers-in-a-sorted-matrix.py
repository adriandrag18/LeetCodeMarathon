# title: Count Negative Numbers in a Sorted Matrix
# timestamp: 2025-06-11 13:53:26
# problemUrl: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# memory: 18.8 MB
# runtime: 0 ms

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        j = n
        count = 0
        for i in range(m):
            while j > 0 and grid[i][j-1] < 0:
                j -= 1
            count += n - j

            if j == 0:
                count += n * (m - i - 1)
                break
        
        return count
        