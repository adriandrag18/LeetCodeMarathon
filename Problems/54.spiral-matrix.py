# title: Spiral Matrix
# timestamp: 2025-06-08 21:11:48
# problemUrl: https://leetcode.com/problems/spiral-matrix/
# memory: 17.6 MB
# runtime: 0 ms

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        lowRow, highRow, lowCol, highCol = 0, m - 1, 0, n - 1

        res = []
        while lowRow < highRow and lowCol < highCol:
            res.extend(matrix[lowRow][lowCol:highCol])
            res.extend([row[highCol] for row in matrix[lowRow:highRow]])
            res.extend(matrix[highRow][highCol:lowCol:-1])
            res.extend([row[lowCol] for row in matrix[highRow:lowRow:-1]])
            lowRow += 1
            lowCol += 1
            highRow -= 1
            highCol -= 1

        if lowRow == highRow and lowCol <= highCol:
            res.extend(matrix[lowRow][lowCol:highCol+1])
        elif lowRow <= highRow and lowCol == highCol:
            res.extend([row[lowCol] for row in matrix[lowRow:highRow+1]])

        return res