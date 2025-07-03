# title: Critical Connections in a Network
# timestamp: 2025-07-03 14:43:23
# problemUrl: https://leetcode.com/problems/critical-connections-in-a-network/
# memory: 68.9 MB
# runtime: 253 ms

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(parent, node):
            nonlocal id
            ids[node] = low[node] = id
            id += 1

            for next in adjList[node]:
                if next == parent:
                    continue
                
                if ids[next] == -1:
                    dfs(node, next)
                    if low[next] > ids[node]:
                        res.append((node, next))
                
                low[node] = min(low[node], low[next])


        adjList = [[] for _ in range(n)]
        for u, v in connections:
            adjList[u].append(v)
            adjList[v].append(u)
        
        ids, low = [-1] * n, [-1] * n
        id = 0
        res = []
        for i in range(n):
            if ids[i] == -1:
                dfs(-1, i)
        
        return res