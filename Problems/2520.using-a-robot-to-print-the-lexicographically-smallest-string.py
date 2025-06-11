# title: Using a Robot to Print the Lexicographically Smallest String
# timestamp: 2025-06-06 15:37:52
# problemUrl: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
# memory: 22.1 MB
# runtime: 354 ms

class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        
        dp = [c for c in s]
        for i in range(n - 2, -1, -1):
            dp[i] = min(dp[i], dp[i+1])

        stack, printed = [], []
        for i in range(n):
            if s[i] == dp[i]:
                printed.append(s[i])
                while stack and i + 1 < n and stack[-1] <= dp[i+1]:
                    printed.append(stack.pop())
                continue
            stack.append(s[i])
        
        printed.extend(stack[::-1])
        return ''.join(printed)