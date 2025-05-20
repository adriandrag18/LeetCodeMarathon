# title: Reverse Bits
# timestamp: 2025-05-20 11:50:06
# problemUrl: https://leetcode.com/problems/reverse-bits/
# memory: 17.7 MB
# runtime: 42 ms

class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:][::-1]
        return int(n, 2) * 2**(32-len(n))