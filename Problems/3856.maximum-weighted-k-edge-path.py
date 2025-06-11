# title: Maximum Weighted K-Edge Path
# timestamp: 2025-06-09 02:18:39
# problemUrl: https://leetcode.com/problems/maximum-weighted-k-edge-path/
# memory: 58.7 MB
# runtime: 742 ms

class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        if k == 0:
            return 0
        if k > n - 1:
            return -1
        _max = -1
        map = {(u, 0): set([0]) for u in range(n)}
        for kk in range(1, k + 1):
            for u in range(n):
                map[(u, kk)] = set()
                for v, w in graph[u]:
                    for val in map.get((v, kk - 1), set()):
                        if val + w >= t:
                            continue
                        map[(u, kk)].add(val + w)
                        if kk == k:
                            _max = max(_max, val + w)
                # print(kk, u, map)
        return _max