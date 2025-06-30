# title: N-th Tribonacci Number
# timestamp: 2025-06-18 00:23:09
# problemUrl: https://leetcode.com/problems/n-th-tribonacci-number/
# memory: 17.6 MB
# runtime: 0 ms

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        trifib = [0] * (n + 1)
        trifib[0], trifib[1], trifib[2] = 0, 1, 1
        
        for i in range(3, n + 1):
            trifib[i] = trifib[i - 1] + trifib[i - 2] + trifib[i - 3]
        
        return trifib[n]