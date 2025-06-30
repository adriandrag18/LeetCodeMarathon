# title: Find the Difference
# timestamp: 2025-06-12 12:05:32
# problemUrl: https://leetcode.com/problems/find-the-difference/
# memory: 17.8 MB
# runtime: 4 ms

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counterS = Counter(s)
        for c in t:
            if counterS.get(c, 0) == 0:
                return c
            counterS[c] -= 1
        
        return -1
