# title: Take K of Each Character From Left and Right
# timestamp: 2024-11-21 01:43:31
# problemUrl: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
# memory: 17.3 MB
# runtime: 253 ms

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1

        if min(count) < k:
            return -1

        res = float("inf")
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] -= 1

            while min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            res = min(res, len(s) - (r - l + 1))
        return res