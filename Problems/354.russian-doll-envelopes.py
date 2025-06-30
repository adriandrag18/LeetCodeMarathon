# title: Russian Doll Envelopes
# timestamp: 2025-06-29 21:56:14
# problemUrl: https://leetcode.com/problems/russian-doll-envelopes/
# memory: 53.1 MB
# runtime: 109 ms

class Solution:
    def maxEnvelopes(self, envs: List[List[int]]) -> int:
        n = len(envs)
        envs.sort(key=lambda x: (x[0] << 17) - x[1])

        dp = [float('inf')] * n
        for i in range(n):
            k = bisect_left(dp, envs[i][1])
            dp[k] = envs[i][1]
            
        return n - dp.count(float('inf'))