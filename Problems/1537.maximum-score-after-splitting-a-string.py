# title: Maximum Score After Splitting a String
# timestamp: 2025-01-01 20:46:55
# problemUrl: https://leetcode.com/problems/maximum-score-after-splitting-a-string/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeros = len(s) - ones

        res = score = ones + (1 if s[0] == '0' else -1)
        for c in s[1:len(s)-1]:
            if c == '0':
                score += 1
                res = max(res, score)
                continue
            score -= 1
        
        return res