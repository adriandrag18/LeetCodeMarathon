# title: Check if a Parentheses String Can Be Valid
# timestamp: 2025-01-13 01:58:33
# problemUrl: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
# memory: 18.8 MB
# runtime: 176 ms

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1 == 1: return False
        
        bMin, bMax = 0, 0  
        
        for i, c in enumerate(s):
            op = c == '('
            wild = locked[i] == '0'
            
            if (not op) or wild: 
                bMin -= 1  
            else: 
                bMin += 1  
            
            if op or wild: 
                bMax += 1  
            else: 
                bMax -= 1  
            
            if bMax < 0: 
                return False
            bMin = max(bMin, 0)

        return bMin == 0