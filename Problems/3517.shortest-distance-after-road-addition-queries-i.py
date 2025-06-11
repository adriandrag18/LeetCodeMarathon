# title: Shortest Distance After Road Addition Queries I
# timestamp: 2024-11-30 01:15:17
# problemUrl: https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/
# memory: 17.8 MB
# runtime: 465 ms

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] for i in range(n)]

        def shortest_path():
            q = deque()
            q.append((0, 0))  # node, length
            visit = set()
            visit.add((0, 0))
            while q:
                cur, length = q.popleft()
                if cur == n - 1:
                    return length
                for nei in adj[cur]:
                    if nei not in visit:
                        q.append((nei, length + 1))
                        visit.add(nei)

        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())
        return res