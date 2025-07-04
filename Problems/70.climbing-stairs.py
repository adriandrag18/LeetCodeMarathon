# title: Climbing Stairs
# timestamp: 2025-01-03 01:00:36
# problemUrl: https://leetcode.com/problems/climbing-stairs/
# memory: 17.6 MB
# runtime: 2 ms

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        a, b = 2, 1
        for i in range(2, n):
            a, b = a + b, a
        
        return a