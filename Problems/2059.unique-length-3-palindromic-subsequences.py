# title: Unique Length-3 Palindromic Subsequences
# timestamp: 2025-01-04 03:48:03
# problemUrl: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
# memory: 18.3 MB
# runtime: 73 ms

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in ascii_lowercase:
            l, r = s.find(c), s.rfind(c)
            if r - l > 1:
                res += len(set(s[l + 1 : r]))
        
        return res
