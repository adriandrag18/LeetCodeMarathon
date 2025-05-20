# title: Sum of Two Integers
# timestamp: 2025-05-20 11:39:52
# problemUrl: https://leetcode.com/problems/sum-of-two-integers/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffff
        a &= mask
        b &= mask
        while b:
            c = (a & b) << 1
            a = (a ^ b) & mask
            b = c & mask
            
        return a if a < 0x8000 else ~(a ^ mask)