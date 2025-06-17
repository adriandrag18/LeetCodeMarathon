# title: Arranging Coins
# timestamp: 2025-06-17 23:38:08
# problemUrl: https://leetcode.com/problems/arranging-coins/
# memory: 17.8 MB
# runtime: 7 ms

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, 2 ** 32 - 1
        while l <= r:
            m = (l + r) // 2
            total = m * (m + 1) // 2
            if n == total:
                return m
            if n < total:
                r = m - 1
            else:
                l = m + 1
        
        return r