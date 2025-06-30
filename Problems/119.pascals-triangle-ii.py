# title: Pascal's Triangle II
# timestamp: 2025-01-03 01:13:57
# problemUrl: https://leetcode.com/problems/pascals-triangle-ii/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row.append(1)
            if len(row) < 3:
                continue
            prev = row[0]
            for i in range(1, len(row) - 1):
                row[i], prev = row[i] + prev, row[i]

        return row 