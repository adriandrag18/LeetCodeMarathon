# title: Count Ways To Build Good Strings
# timestamp: 2024-12-30 11:24:54
# problemUrl: https://leetcode.com/problems/count-ways-to-build-good-strings/
# memory: 22.4 MB
# runtime: 94 ms

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7

        dp = [1] + [0] * (high + 1)
        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] += dp[i-zero]
            if i - one >= 0:
                dp[i] += dp[i-one]
            dp[i] %= mod
        
        return sum(dp[low:high+1]) % mod