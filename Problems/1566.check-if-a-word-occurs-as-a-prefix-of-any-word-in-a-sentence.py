# title: Check If a Word Occurs As a Prefix of Any Word in a Sentence
# timestamp: 2024-12-02 23:25:01
# problemUrl: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# memory: 17.5 MB
# runtime: 0 ms

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words):
            if searchWord == word[:min(len(searchWord), len(word))]:
                return i + 1
        return -1
        