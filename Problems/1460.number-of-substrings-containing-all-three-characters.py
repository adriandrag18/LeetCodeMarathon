# title: Number of Substrings Containing All Three Characters
# timestamp: 2025-03-11 17:08:54
# problemUrl: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# memory: 18.1 MB
# runtime: 448 ms

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r, count, n = 0, 0, 0, len(s)
        map = {}
        while r < n:
            map[s[r]] = map.get(s[r], 0) + 1
            r += 1
            # print(r, map)
            if not all((map.get(c, 0) > 0 for c in 'abc')):
                continue
            
            while all((map.get(c, 0) > 0 for c in 'abc')):
                count += n - r + 1
                map[s[l]] -= 1
                l += 1
                # print(l, r, map, count)
        
        return count