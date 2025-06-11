# title: Decode Ways
# timestamp: 2025-05-20 18:41:09
# problemUrl: https://leetcode.com/problems/decode-ways/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 1)
        if s[0] == '0':
            return 0
        if s[-1] == '0':
            dp[-1] = 0
        
        for i in range(len(s) - 2, -1, -1):
            a, b = int(s[i]), int(s[i + 1])
            dp[i] = dp[i + 1]

            if ((a == 2 and b <= 6) or a == 1) and b != 0:
                dp[i] += dp[i + 2]
            elif b == 0:
                if a not in (1, 2):
                    return 0
                dp[i + 1] = 0
        
        print(dp)
        return dp[0]

