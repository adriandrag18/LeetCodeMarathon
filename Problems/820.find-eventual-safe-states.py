# title: Find Eventual Safe States
# timestamp: 2025-06-02 12:34:58
# problemUrl: https://leetcode.com/problems/find-eventual-safe-states/
# memory: 23.9 MB
# runtime: 52 ms

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = set()
        notSafe = set()
        n = len(graph)
        
        for i, adjList in enumerate(graph):
            if not adjList:
                safe.add(i)
        
        def dfs(path, node):
            # if node == 2: print(safe, notSafe, path)
            if node in notSafe:
                return False
            
            if node in path:
                notSafe.add(node)
                return False
            
            if node in safe:
                return True
            
            # if node == 2 or node == 3: print(node, safe, notSafe, path)
            path.add(node)
            for nextNode in graph[node]:
                if not dfs(path, nextNode):
                    notSafe.add(node)
                    return False
            
            # if node == 2 or node == 3: print(node, safe, notSafe, path)
            safe.add(node)
            path.remove(node)

            return True
        
        for i in range(n):
            dfs(set(), i)
        
        return sorted(list(safe))
        
        