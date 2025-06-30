# title: Total Characters in String After Transformations I
# timestamp: 2025-05-13 11:40:18
# problemUrl: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
# memory: 22.1 MB
# runtime: 54 ms

mod = 10**9 + 7
dp = [1] * (10**5 + 26)
for i in range(26, len(dp)):
    dp[i] = (dp[i-26] + dp[i-25]) % mod

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        def toNum(char):
            return ord(char) - ord('a')
        
        total = 0
        for k, v in Counter(s).items():
            total = (total + v * dp[toNum(k) + t]) % mod
        return total

        