# title: Find the Maximum Sum of Node Values
# timestamp: 2025-05-23 14:59:03
# problemUrl: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
# memory: 26.4 MB
# runtime: 42 ms

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        # edgesMap = {}
        # for u, v in edges:
        #     edgesMap[u] = v
        #     edgesMap[v] = v
        # n = len(nums)
        # dp = [{} for _ in range(n)]
        
        # for node in range(n - 1, -1, -1):
        #     dp[node][False] = nums[node]
        #     dp[node][True] = nums[node] ^ k
        #     diff = nums[node] - nums[node] ^ k
        #     for child in edgesMap[node]:
        #         if child < node:
        #             continue
        #         dp[node][False] += max(dp[child][False], dp[child][True] + diff)

        diffs = sorted([(num ^ k) - num for num in nums], reverse=True)
        gain = 0
        
        for i in range(0, len(diffs), 2):
            if diffs[i] < 0: break
            gain += max(diffs[i] + diffs[i+1] if i + 1 < len(nums) else 0, 0)
            
        return sum(nums) + gain