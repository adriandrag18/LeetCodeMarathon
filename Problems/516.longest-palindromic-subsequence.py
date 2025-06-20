# title: Longest Palindromic Subsequence
# timestamp: 2025-06-20 10:47:21
# problemUrl: https://leetcode.com/problems/longest-palindromic-subsequence/
# memory: 89.7 MB
# runtime: 497 ms

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        def help(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if dp[l][r]:
                return dp[l][r]
            
            if s[l] == s[r]:
                dp[l][r] = 2 + help(l + 1, r - 1)
            else:
                dp[l][r] = max(help( l + 1, r), help(l, r - 1))
            
            return dp[l][r]
        
        return help(0, n - 1)