# title: Unique Binary Search Trees
# timestamp: 2025-06-29 22:07:51
# problemUrl: https://leetcode.com/problems/unique-binary-search-trees/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        
        return dp[n]
    