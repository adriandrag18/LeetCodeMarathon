# title: Maximum Number of K-Divisible Components
# timestamp: 2024-12-21 03:58:21
# problemUrl: https://leetcode.com/problems/maximum-number-of-k-divisible-components/
# memory: 40.6 MB
# runtime: 119 ms

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        def dfs(u, p):
            nonlocal ans
            subtree_sum = values[u]
            for v in adj[u]:
                if v != p:
                    subtree_sum += dfs(v, u)
            if subtree_sum % k == 0:
                ans += 1
                return 0
            return subtree_sum

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = 0
        dfs(0, -1)
        return ans