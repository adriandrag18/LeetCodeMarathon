# title: Longest Palindromic Substring
# timestamp: 2025-01-06 22:37:12
# problemUrl: https://leetcode.com/problems/longest-palindromic-substring/
# memory: 25.5 MB
# runtime: 1498 ms

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res, m = (0, 0), 1
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if m < j - i + 1:
                        m, res = j - i + 1, (i, j)
        # print(*dp, sep='\n')
        
        return s[res[0]:res[1] + 1]