# title: Word Break
# timestamp: 2025-05-24 13:21:08
# problemUrl: https://leetcode.com/problems/word-break/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i, isPossible in enumerate(dp):
            if not isPossible:
                continue
            for w in wordDict:
                if i + len(w) > len(s):
                    continue
                if w == s[i:i + len(w)]:
                    dp[i + len(w)] = True
        
        return dp[-1]
            