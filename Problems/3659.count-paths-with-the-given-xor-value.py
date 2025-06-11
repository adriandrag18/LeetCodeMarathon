# title: Count Paths With the Given XOR Value
# timestamp: 2024-12-22 17:52:48
# problemUrl: https://leetcode.com/problems/count-paths-with-the-given-xor-value/
# memory: 780.8 MB
# runtime: 4048 ms

class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        mod, n, m = 10 ** 9 + 7, len(grid), len(grid[0])
        dp = {}

        def solve(i, j, curr):
            if i >= n or j >= m:
                return 0
            
            newCurr = grid[i][j] ^ curr
            if i == n - 1 and j == m - 1:
                return 1 if newCurr == k else 0
            
            if (i, j, curr) in dp:
                return dp[(i, j, curr)]
            
            down = solve(i + 1, j, newCurr)
            right = solve(i, j + 1, newCurr)
            dp[(i, j, curr)] = (down + right) % mod

            return dp[(i, j, curr)]
        
        return solve(0, 0, 0)