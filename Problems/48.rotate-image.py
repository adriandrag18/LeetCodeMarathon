# title: Rotate Image
# timestamp: 2025-06-07 13:41:34
# problemUrl: https://leetcode.com/problems/rotate-image/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def swap(i, j):
            matrix[i][j], matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i] = matrix[n - 1 - j][i], matrix[n - 1 - i][n - 1 - j], matrix[j][n - 1 - i], matrix[i][j]
        
        for i in range((n + 1) // 2):
            for j in range(i, n - 1 - i):
                swap(i, j)
            # print(*matrix, sep='\n', end='\n\n')
        