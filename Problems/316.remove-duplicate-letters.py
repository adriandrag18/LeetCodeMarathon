# title: Remove Duplicate Letters
# timestamp: 2025-05-20 11:03:41
# problemUrl: https://leetcode.com/problems/remove-duplicate-letters/
# memory: 18 MB
# runtime: 3 ms

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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
        