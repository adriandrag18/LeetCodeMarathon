# title: Pascal's Triangle
# timestamp: 2025-01-03 01:05:16
# problemUrl: https://leetcode.com/problems/pascals-triangle/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([1] * (i + 1))
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        
        return res