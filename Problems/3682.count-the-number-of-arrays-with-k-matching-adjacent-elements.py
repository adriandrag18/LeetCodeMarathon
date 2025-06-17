# title: Count the Number of Arrays with K Matching Adjacent Elements
# timestamp: 2025-06-17 16:52:14
# problemUrl: https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/
# memory: 18.1 MB
# runtime: 3641 ms

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # m * (1 * 1 * ... * 1) * ((m - 1) * (m - 1) * ... * (m - 1))
        # m * (m - 1) ** (n - k - 1) * (n - 1)! / ((n - k - 1)! * k!)
        mod = 10**9 + 7
        
        res =  m
        for _ in range(n - k - 1):
            res = res * (m - 1) % mod
        
        return (comb(n - 1, k) % mod) * res % mod