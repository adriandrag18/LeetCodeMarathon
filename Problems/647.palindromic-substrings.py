# title: Palindromic Substrings
# timestamp: 2025-05-20 15:27:39
# problemUrl: https://leetcode.com/problems/palindromic-substrings/
# memory: 17.6 MB
# runtime: 159 ms

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        for i in range(0, len(s) - 1):
            j = 1
            while 0 <= i - j and i + j < len(s) and s[i + j] == s[i - j]:
                j += 1
            res += j - 1
            
            if s[i] != s[i + 1]:
                continue
            
            j = 1
            while 0 <= i - j and i + j + 1 < len(s) and s[i + j + 1] == s[i - j]:
                j += 1
            res += j
        
        return res