# title: Valid Perfect Square
# timestamp: 2025-06-13 23:15:32
# problemUrl: https://leetcode.com/problems/valid-perfect-square/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, 2**16
        while l <= r:
            m = (l + r) // 2
            test = m * m
            if test == num:
                return True
            if test < num:
                l = m + 1
            else:
                r = m - 1
        
        return False