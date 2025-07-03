# title: Similar String Groups
# timestamp: 2025-07-03 15:04:43
# problemUrl: https://leetcode.com/problems/similar-string-groups/
# memory: 18.2 MB
# runtime: 117 ms

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def check(u, v):
            count = 0
            for a, b in zip(u, v):
                if a != b:
                    count += 1
                    if count > 2:
                        return False
            
            return count in [0, 2]
        
        n = len(strs)
        parent = list(range(n))
        def find(u):
            while u != parent[u]:
                u = parent[u]
            return u
        
        def union(u, v):
            parent[find(v)] = find(u)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if check(strs[i], strs[j]):
                    union(i, j)
        
        count = 0
        for i in range(n):
            if i == find(i):
                count += 1

        return count
            