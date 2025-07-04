# title: Maximal Network Rank
# timestamp: 2025-06-24 00:33:02
# problemUrl: https://leetcode.com/problems/maximal-network-rank/
# memory: 19.2 MB
# runtime: 34 ms

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        map = defaultdict(set)
        for a, b in roads:
            map[a].add(b)
            map[b].add(a)
        
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = max(res, len(map[i]) + len(map[j]) - (1 if i in map[j] else 0))
        
        return res
