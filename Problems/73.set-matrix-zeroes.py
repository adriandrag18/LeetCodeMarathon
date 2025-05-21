# title: Set Matrix Zeroes
# timestamp: 2025-05-21 05:52:06
# problemUrl: https://leetcode.com/problems/set-matrix-zeroes/
# memory: 18.7 MB
# runtime: 0 ms

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        for i, line in enumerate(matrix):
            for j, el in enumerate(line):
                if not el:
                    rows.add(i)
                    cols.add(j)

        rows = list(rows)
        cols = list(cols)
        print(rows, cols)

        while rows:
            i = rows.pop()
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

        while cols:
            j = cols.pop()
            for i in range(len(matrix)):
                matrix[i][j] = 0
        
        # print(*matrix, sep='\n')
