# title: Number of Ways to Arrive at Destination
# timestamp: 2025-03-25 17:04:24
# problemUrl: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
# memory: 25.3 MB
# runtime: 28 ms

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for r in roads:
            adjList[r[0]].append((r[1], r[2]))
            adjList[r[1]].append((r[0], r[2]))
        
        mod = 10**9+7
        minCost, res = float('inf'), 0
        dist = {node: (float('inf'), 1) for node in range(n)}
        dist[0] = (0, 1)
        seen = set()
        queue = [(0, 0)]
        while queue:
            cost, node = heappop(queue)
            ways = dist[node][1]
            if node in seen:
                continue
            seen.add(node)

            for nn, c in adjList[node]:
                if nn in seen:
                    continue
                newCost = cost + c
                if newCost > minCost:
                    continue
                if dist[nn][0] > newCost:
                    dist[nn] = (newCost, ways)
                    heappush(queue, (newCost, nn))
                    if nn == n - 1:
                        minCost = newCost
                elif dist[nn][0] == newCost:
                    dist[nn] = (newCost, (ways + dist[nn][1]) % mod)
        
        # print(dist)

        return dist[n-1][1]