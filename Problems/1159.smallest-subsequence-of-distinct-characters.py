# title: Smallest Subsequence of Distinct Characters
# timestamp: 2025-05-20 11:04:30
# problemUrl: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# memory: 17.8 MB
# runtime: 1 ms

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        lastIndexOf = {}
        for i, c in enumerate(s):
            lastIndexOf[c] = i
        
        res = []
        for i, c in enumerate(s):
            if c in res:
                continue
            
            while res and res[-1] > c and lastIndexOf[res[-1]] > i:
                res.pop()
                
            res.append(c)
        
        return ''.join(res)