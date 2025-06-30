# title: Minimize the Maximum Edge Weight of Graph
# timestamp: 2025-01-12 06:58:05
# problemUrl: https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/
# memory: 76.7 MB
# runtime: 1659 ms

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        adjList = [[] for _ in range(n)]
        ma = -1
        for a, b, w in edges:
            adjList[b].append((a, w))
            ma = max(ma, w)
        # print(adjList)
        def dfs(node, m, seen):
            seen.add(node)
            no = 1
            for new, w in adjList[node]:
                if w > m or new in seen:
                    continue
                no += dfs(new, m, seen)
                if no == n:
                    break
            return no

        l, r = 0, ma
        while l <= r:
            m = (l + r) // 2
            seen = set()
            res = dfs(0, m, seen)
            # print(l, m, r, res)
            if res == n:
                r = m - 1
                continue
            l = m + 1
        
        return l if l != ma + 1 else -1
