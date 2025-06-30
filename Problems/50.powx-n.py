# title: Pow(x, n)
# timestamp: 2025-06-17 23:57:26
# problemUrl: https://leetcode.com/problems/powx-n/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 1
        res = 1
        if n < 0:
            sign = -1
            n = -n
        if n == 0:
            return 1
        
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        
        if sign == -1:
            return 1 / res
        return res