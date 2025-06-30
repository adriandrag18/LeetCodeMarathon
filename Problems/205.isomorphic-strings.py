# title: Isomorphic Strings
# timestamp: 2025-01-13 19:04:37
# problemUrl: https://leetcode.com/problems/isomorphic-strings/
# memory: 18.1 MB
# runtime: 3 ms

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        seen = set()
        for a, b in zip(s, t):
            if a not in map:
                if b in seen:
                    return False
                map[a] = b
                seen.add(b)
            
            test = map[a]
            if b != test:
                return False
            
        return True