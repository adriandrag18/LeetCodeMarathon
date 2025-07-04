# title: Triangle
# timestamp: 2025-06-14 16:41:32
# problemUrl: https://leetcode.com/problems/triangle/
# memory: 18.7 MB
# runtime: 1 ms

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n 
        old = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(0, i + 1):
                dp[j] = triangle[i][j] + min(old[j], old[j+1])
            old, dp = dp, [0] * (i + 1)
        
        return old[0]