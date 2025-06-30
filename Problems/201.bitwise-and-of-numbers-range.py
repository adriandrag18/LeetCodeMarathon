# title: Bitwise AND of Numbers Range
# timestamp: 2025-06-21 19:16:32
# problemUrl: https://leetcode.com/problems/bitwise-and-of-numbers-range/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        n = 1
        while right - left >= n:
            n *= 2
        
        n = ((2 << 32) - 1) ^ (n - 1)
        
        return left & right & n
    