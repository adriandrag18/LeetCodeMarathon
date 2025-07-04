# title: Largest Color Value in a Directed Graph
# timestamp: 2025-07-04 12:13:55
# problemUrl: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
# memory: 116.4 MB
# runtime: 1948 ms

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        for s, d in edges:
            graph[s].append(d)

        colors = [ord(c) - ord('a') for c in colors]
        nColors = max(colors) + 1
        dp = [[0] * nColors for _ in range(n)]
        seen = set()
        
        def dfs(node, path):
            if node in path:
                return False
            path.add(node)

            if node in seen:
                path.remove(node) 
                return True
            seen.add(node)
            
            dp[node][colors[node]] = 1

            for next in graph[node]:
                if not dfs(next, path):
                    return False
                for color in range(nColors):
                    dp[node][color] = max(dp[node][color], dp[next][color] + (1 if color == colors[node] else 0))
            
            path.remove(node)
            return True
        
        for node in range(n):
            if not dfs(node, set()):
                return -1

        return max([max(el) for el in dp])
