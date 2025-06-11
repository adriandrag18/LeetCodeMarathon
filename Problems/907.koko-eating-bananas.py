# title: Koko Eating Bananas
# timestamp: 2024-12-12 17:42:25
# problemUrl: https://leetcode.com/problems/koko-eating-bananas/
# memory: 18.3 MB
# runtime: 123 ms

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = max(1, sum(piles) // h), max(piles)
        while l <= r:
            m = (l + r) // 2
            s = 0
            for x in piles:
                s += (x - 1) // m
            if s + len(piles) <= h:
                r = m - 1
                continue
            l = m + 1
        
        return l