# title: Minimum Height Trees
# timestamp: 2025-06-18 00:21:34
# problemUrl: https://leetcode.com/problems/minimum-height-trees/
# memory: 25.4 MB
# runtime: 81 ms

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        counts = [0] * n
        links = [0] * n
        for edge in edges:
            links[edge[0]] ^= edge[1]
            counts[edge[0]] += 1
            links[edge[1]] ^= edge[0]
            counts[edge[1]] += 1
        
        Qu = []
        dists = [0] * n
        for i in range(n):
            if counts[i] == 1:
                Qu.append(i)
        
        stp = 1
        while Qu:
            size = len(Qu)
            for _ in range(size):
                tmp = Qu.pop(0)
                neighbor = links[tmp]
                links[neighbor] ^= tmp
                counts[neighbor] -= 1
                if counts[neighbor] == 1:
                    dists[neighbor] = max(stp, dists[neighbor])
                    Qu.append(neighbor)
            stp += 1
        
        maxDist = max(dists)
        res = [i for i, dist in enumerate(dists) if dist == maxDist]
        
        return res