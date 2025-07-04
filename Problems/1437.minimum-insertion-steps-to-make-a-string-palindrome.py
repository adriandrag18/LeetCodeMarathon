# title: Minimum Insertion Steps to Make a String Palindrome
# timestamp: 2025-06-30 11:48:17
# problemUrl: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
# memory: 17.9 MB
# runtime: 264 ms

class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        prev, dp = [1], [0, 0]
        for i in range(1, n):
            dp[-1] = 1
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[j] = 2 + (prev[j+1] if i - j >= 2 else 0)
                else:
                    dp[j] = max(prev[j], dp[j+1])
            prev, dp = dp, [0] * (i + 2)
            
        return n - prev[0]

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        def help(l, r):
            if l > r:
                return 0
            if l == r:
                dp[l][r] = 1
                return 1
            if dp[l][r]:
                return dp[l][r]
            
            if s[l] == s[r]:
                dp[l][r] = 2 + help(l + 1, r - 1)
            else:
                dp[l][r] = max(help( l + 1, r), help(l, r - 1))
            
            return dp[l][r]
        
        res = help(0, n - 1)
        # print(*dp, sep='\n')
        return n - res