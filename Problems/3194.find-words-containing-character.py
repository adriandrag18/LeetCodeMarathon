# title: Find Words Containing Character
# timestamp: 2025-05-24 12:48:43
# problemUrl: https://leetcode.com/problems/find-words-containing-character/
# memory: 17.6 MB
# runtime: 0 ms

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, w in enumerate(words) if x in w]