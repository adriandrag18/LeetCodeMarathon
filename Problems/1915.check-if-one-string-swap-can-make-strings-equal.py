# title: Check if One String Swap Can Make Strings Equal
# timestamp: 2025-02-06 11:56:06
# problemUrl: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = [(a, b) for a, b in zip(s1, s2) if a != b]
        
        if len(diffs) == 0:
            return True
        if len(diffs) == 2:
            a, b = diffs[0]
            c, d = diffs[1]
            if a == d and c == b:
                return True
        
        return False