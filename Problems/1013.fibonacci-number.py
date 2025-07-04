# title: Fibonacci Number
# timestamp: 2025-06-03 13:25:08
# problemUrl: https://leetcode.com/problems/fibonacci-number/
# memory: 17.7 MB
# runtime: 36 ms

f = [0, 1] + [-1] * 31
class Solution:
    def fib(self, n: int) -> int:
        if f[n] != -1:
            return f[n]
            
        f[n] = self.fib(n - 1) + self.fib(n - 2)
        return f[n]
