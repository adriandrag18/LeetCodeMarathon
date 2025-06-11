# title: Loud and Rich
# timestamp: 2025-06-05 01:30:15
# problemUrl: https://leetcode.com/problems/loud-and-rich/
# memory: 24.6 MB
# runtime: 20 ms

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)
        
        res = [-1] * n
        def dfs(node):
            if res[node] == -1:
                res[node] = min([dfs(i) for i in graph[node]] + [node], key=lambda x: quiet[x])
            return res[node]
    
        return [dfs(i) for i in range(n)]
    