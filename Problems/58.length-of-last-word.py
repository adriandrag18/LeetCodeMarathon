# title: Length of Last Word
# timestamp: 2025-06-09 14:30:59
# problemUrl: https://leetcode.com/problems/length-of-last-word/
# memory: 17.6 MB
# runtime: 0 ms

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])