# title: Find Missing and Repeated Values
# timestamp: 2025-03-06 14:44:23
# problemUrl: https://leetcode.com/problems/find-missing-and-repeated-values/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        a = 0
        arr = [0] * (n * n)
        for line in grid:
            for el in line:
                arr[el-1] += 1
                if arr[el-1] == 2:
                    a = el

        return [a, arr.index(0) + 1]