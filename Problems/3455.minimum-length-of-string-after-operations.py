# title: Minimum Length of String After Operations
# timestamp: 2025-01-13 18:55:03
# problemUrl: https://leetcode.com/problems/minimum-length-of-string-after-operations/
# memory: 19 MB
# runtime: 143 ms

class Solution:
    def minimumLength(self, s: str) -> int:
        return sum([(c - 1) % 2 + 1 for c in Counter(s).values()])