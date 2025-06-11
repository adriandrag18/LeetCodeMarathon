# title: Count Total Number of Colored Cells
# timestamp: 2025-03-05 10:49:47
# problemUrl: https://leetcode.com/problems/count-total-number-of-colored-cells/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 2 * (n - 1) * n