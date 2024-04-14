# title: Merge Strings Alternately
# timestamp: 2024-04-14 21:11:17
# problemUrl: https://leetcode.com/problems/merge-strings-alternately/
# memory: 16.6 MB
# runtime: 32 ms

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        letters = []
        for i in range(min(len(word1), len(word2))):
            letters.extend([word1[i], word2[i]])
        
        letters.extend([word1[min(len(word1), len(word2)):], word2[min(len(word1), len(word2)):]])
        
        return "".join(letters)