# title: Redundant Connection
# timestamp: 2025-06-22 18:11:13
# problemUrl: https://leetcode.com/problems/redundant-connection/
# memory: 18.1 MB
# runtime: 1 ms

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        def find(u):
            while u not in parent or parent[u] != u:
                if u not in parent:
                    parent[u] = u
                    break
                u = parent[u]

            return u
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            
            parent[pv] = pu
            return True
        
        res = []
        for u, v in edges:
            if not union(u, v):
                res = [u, v]
        
        return res