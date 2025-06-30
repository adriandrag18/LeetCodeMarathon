# title: Maximum Length of Pair Chain
# timestamp: 2025-06-23 23:59:23
# problemUrl: https://leetcode.com/problems/maximum-length-of-pair-chain/
# memory: 18.1 MB
# runtime: 7 ms

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        map = {}
        for l, r in pairs:
            if l not in map:
                map[l] = r
                continue
            map[l] = min(map[l], r)
        
        pairs = sorted(map.items(), key=lambda x: x[1])
        
        curr, res = -float('inf'), 0
        for l, r in pairs:
            if curr < l:
                curr = r
                res += 1
        
        return res