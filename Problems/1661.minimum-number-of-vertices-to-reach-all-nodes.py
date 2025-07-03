# title: Minimum Number of Vertices to Reach All Nodes
# timestamp: 2025-07-03 14:46:09
# problemUrl: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
# memory: 44.8 MB
# runtime: 11 ms

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for s, d in edges:
            indegree[d] += 1
        
        res = []
        for node in range(n):
            if not indegree[node]:
                res.append(node)

        return res
