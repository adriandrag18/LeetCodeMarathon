# title: Gas Station
# timestamp: 2025-06-10 19:17:48
# problemUrl: https://leetcode.com/problems/gas-station/
# memory: 23.4 MB
# runtime: 32 ms

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        _min, res = 0, 0
        curr = 0
        for i, (c, g) in enumerate(zip(cost, gas)):
            curr += g - c
            if curr < _min:
                _min = curr
                res = i + 1 % len(cost)
        
        if curr < 0:
            return -1
        
        return res