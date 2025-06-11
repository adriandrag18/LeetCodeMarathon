# title: Maximum XOR for Each Query
# timestamp: 2024-11-08 02:20:59
# problemUrl: https://leetcode.com/problems/maximum-xor-for-each-query/
# memory: 32.4 MB
# runtime: 43 ms

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        print(bin(mask))
        xor = 0
        for el in nums:
            xor ^= el
        
        res = []
        for el in nums[::-1]:
            n = xor & mask
            n ^= mask
            res.append(n)
            xor ^= el
        return res
