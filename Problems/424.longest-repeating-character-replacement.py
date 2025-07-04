# title: Longest Repeating Character Replacement
# timestamp: 2024-11-05 22:13:32
# problemUrl: https://leetcode.com/problems/longest-repeating-character-replacement/
# memory: 16.8 MB
# runtime: 35 ms

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = min(k + 1, len(s))
        
        d = {}
        for c in s[:l]:
            d[c] = d.get(c, 0) + 1
        
        m = max(d.values())
        # print(d, m)

        i = 0
        while i + l < len(s):
            while l <= k + m:
                d[s[i+l]] = d.get(s[i+l], 0) + 1
                m = max(m, d[s[i+l]])
                l += 1
                if i + l == len(s):
                    break
            l -= 1
            d[s[i]] -= 1
            i += 1

        return min(k + m, len(s))