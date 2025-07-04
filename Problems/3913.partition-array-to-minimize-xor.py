# title: Partition Array to Minimize XOR
# timestamp: 2025-06-29 07:06:39
# problemUrl: https://leetcode.com/problems/partition-array-to-minimize-xor/
# memory: 19 MB
# runtime: 18268 ms

class Solution:
    def minXor(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            return reduce(operator.xor, nums)
        if k == n:
            return max(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] ^ nums[i]

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        
        for m in range(1, k + 1):
            for i in range(m, n + 1):
                if m == 1:
                    dp[i][m] = pref[i]
                else:
                    for j in range(m - 1, i):
                        val = pref[i] ^ pref[j]
                        dp[i][m] = min(dp[i][m], max(dp[j][m - 1], val))
        
        return dp[n][k]
        