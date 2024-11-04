# title: Longest Substring Without Repeating Characters
# timestamp: 2024-11-04 19:21:30
# problemUrl: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# memory: 16.7 MB
# runtime: 6 ms

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        map = {}
        l, res = 0, 0
        for r in range(len(s)):
            c = s[r]
            if c in map and l <= map[c]:
                l = map[c] + 1
            else:
                res = max(res, r - l + 1)
            map[c] = r

        return res