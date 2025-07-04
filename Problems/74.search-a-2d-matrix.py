# title: Search a 2D Matrix
# timestamp: 2024-12-12 11:49:01
# problemUrl: https://leetcode.com/problems/search-a-2d-matrix/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        N = m * n
        def get(i):
            return matrix[i // n][i % n]
        
        l, r = 0, N - 1
        while l <= r:
            m = (l + r) // 2
            if get(m) == target:
                return True
            if get(m) < target:
                l = m + 1
                continue
            r = m - 1
        
        return False