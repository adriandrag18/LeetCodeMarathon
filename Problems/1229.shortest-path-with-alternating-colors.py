# title: Shortest Path with Alternating Colors
# timestamp: 2025-06-06 17:58:28
# problemUrl: https://leetcode.com/problems/shortest-path-with-alternating-colors/
# memory: 17.8 MB
# runtime: 6 ms

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        shortest = [[float('inf'), float('inf')] for _ in range(n)]
        shortest[0] = [0, 0]

        graph = [[[], []] for _ in range(n)]
        for a, b in redEdges:
            graph[a][0].append(b)
        for a, b in blueEdges:
            graph[a][1].append(b)
        
        queue = deque([(0, 0), (0, 1)])
        while queue:
            node, color = el = queue.popleft()
            color = 1 - color
            for nei in graph[node][color]:
                if shortest[nei][color] != float('inf'):
                    continue
                shortest[nei][color] = shortest[node][1-color] + 1
                queue.append((nei, color))
            
        return [min(s[0], s[1]) if min(s[0], s[1]) != float('inf') else -1 for s in shortest]
