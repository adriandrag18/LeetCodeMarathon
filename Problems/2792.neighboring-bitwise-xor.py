# title: Neighboring Bitwise XOR
# timestamp: 2025-01-18 01:29:01
# problemUrl: https://leetcode.com/problems/neighboring-bitwise-xor/
# memory: 22.4 MB
# runtime: 54 ms

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        for first in [1, 2]:
            prev = first
            for d in derived:
                if d:
                    prev = ~prev
            if prev == first:
                return True
        
        return False