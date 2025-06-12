# title: Repeated Substring Pattern
# timestamp: 2025-06-12 20:17:42
# problemUrl: https://leetcode.com/problems/repeated-substring-pattern/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        test = s[1:] + s[:-1]
        return s in test