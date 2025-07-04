# title: Find Valid Pair of Adjacent Digits in String
# timestamp: 2025-02-01 16:33:47
# problemUrl: https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/
# memory: 17.9 MB
# runtime: 7 ms

class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)
        for i in range(1, len(s)):
            if s[i-1] != s[i] and counter[s[i-1]] == int(s[i-1]) and counter[s[i]] == int(s[i]):
                return s[i-1:i+1]
        
        return ""