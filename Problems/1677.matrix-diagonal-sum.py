# title: Matrix Diagonal Sum
# timestamp: 2025-06-12 22:16:24
# problemUrl: https://leetcode.com/problems/matrix-diagonal-sum/
# memory: 18.4 MB
# runtime: 1 ms

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        return sum([mat[i][i] + mat[i][n-i-1] for i in range(n)]) - (mat[n // 2][ n // 2] if n % 2 else 0)