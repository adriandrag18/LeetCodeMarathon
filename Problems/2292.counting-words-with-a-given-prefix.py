# title: Counting Words With a Given Prefix
# timestamp: 2025-01-09 14:30:00
# problemUrl: https://leetcode.com/problems/counting-words-with-a-given-prefix/
# memory: 18.1 MB
# runtime: 0 ms

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([1 for word in words if word.find(pref) == 0])