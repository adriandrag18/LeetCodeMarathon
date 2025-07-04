# title: Minimum Flips to Make a OR b Equal to c
# timestamp: 2025-01-03 02:08:38
# problemUrl: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
# memory: 18 MB
# runtime: 33 ms

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:][::-1]
        b = bin(b)[2:][::-1]
        c = bin(c)[2:][::-1]
        n = max([len(a), len(b), len(c)])
        a += '0' * (n - len(a))
        b += '0' * (n - len(b))
        c += '0' * (n - len(c))
        
        res = 0
        for a, b, c in zip(a, b, c):
            n = (a + b).count('1')
            if c == '1':
                if n == 0:
                    res += 1
                continue
            res += n

        return res