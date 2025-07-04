# title: Is Graph Bipartite?
# timestamp: 2025-07-04 11:36:40
# problemUrl: https://leetcode.com/problems/is-graph-bipartite/
# memory: 18.4 MB
# runtime: 4 ms

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        for i in range(n):
            if color[i]:
                continue

            color[i] = 1    
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for next in graph[node]:
                    if color[next] == color[node]:
                        return False
                    if not color[next]:
                        color[next] = -color[node]
                        queue.append(next)

        return True
