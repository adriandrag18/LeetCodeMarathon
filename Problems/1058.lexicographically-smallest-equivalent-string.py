# title: Lexicographically Smallest Equivalent String
# timestamp: 2025-06-05 12:02:26
# problemUrl: https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# memory: 17.9 MB
# runtime: 4 ms

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}
        def find(char):
            if char not in parent:
                return char
            return find(parent[char])
        
        def merge(char1, char2):
            p1, p2 = find(char1), find(char2)
            if p1 == p2:
                return
            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
        
        for a, b in zip(s1, s2):
            merge(a, b)
        
        res = [find(char) for char in baseStr]

        return ''.join(res)
