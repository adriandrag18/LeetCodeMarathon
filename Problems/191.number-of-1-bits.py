# title: Number of 1 Bits
# timestamp: 2025-05-20 11:47:42
# problemUrl: https://leetcode.com/problems/number-of-1-bits/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')