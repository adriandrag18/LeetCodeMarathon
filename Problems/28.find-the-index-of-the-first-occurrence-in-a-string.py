# title: Find the Index of the First Occurrence in a String
# timestamp: 2025-06-09 14:29:59
# problemUrl: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)