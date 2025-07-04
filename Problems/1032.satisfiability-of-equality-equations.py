# title: Satisfiability of Equality Equations
# timestamp: 2025-06-10 23:43:37
# problemUrl: https://leetcode.com/problems/satisfiability-of-equality-equations/
# memory: 18.2 MB
# runtime: 4 ms

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def i(c):
            return ord(c) - ord('a')

        edges = []
        parent = list(range(26))
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a
    
        def union(a, b):
            parent[find(b)] = find(a)

        for eq in equations:
            a, b = i(eq[0]), i(eq[3])
            if eq[1] == '=':
                print(a, b)
                if a != b:
                    union(a, b)
            else:
                if a == b:
                    return False
                edges.append((a, b))
                
        for a, b in edges:
            if find(a) == find(b):
                return False
        
        return True
