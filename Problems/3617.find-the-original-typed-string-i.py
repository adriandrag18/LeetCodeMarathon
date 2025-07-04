# title: Find the Original Typed String I
# timestamp: 2025-07-02 10:23:16
# problemUrl: https://leetcode.com/problems/find-the-original-typed-string-i/
# memory: 17.9 MB
# runtime: 27 ms

class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = ''
        count = 1
        for c in word:
            if c == prev:
                count += 1
            else:
                prev = c

        return count