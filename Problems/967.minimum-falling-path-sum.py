# title: Minimum Falling Path Sum
# timestamp: 2025-06-19 13:01:43
# problemUrl: https://leetcode.com/problems/minimum-falling-path-sum/
# memory: 18.7 MB
# runtime: 15 ms

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        partial = [float('inf')] * (n + 1)
        prev = [float('inf')] + matrix[-1]

        for i in range(n - 2, -1, -1):
            for j in range(1, n + 1):
                partial[j] = matrix[i][j-1] + min(prev[j-1:j+2])
            prev, partial = partial, [float('inf')] * (n + 1)
        
        return min(prev)