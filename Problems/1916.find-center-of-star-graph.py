# title: Find Center of Star Graph
# timestamp: 2025-05-24 15:04:15
# problemUrl: https://leetcode.com/problems/find-center-of-star-graph/
# memory: 45.6 MB
# runtime: 0 ms

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen = set()
        for u, v in edges:
            if u in seen:
                return u
            seen.add(u)
            if v in seen:
                return v
            seen.add(v)
        
        return -1
            