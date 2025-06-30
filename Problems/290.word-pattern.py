# title: Word Pattern
# timestamp: 2025-06-04 17:24:34
# problemUrl: https://leetcode.com/problems/word-pattern/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False
        
        map = {} 
        for char, word in zip(pattern, words):
            if char in map and map[char] != word:
                return False
            map[char] = word
        
        return len(map.keys()) == len(set(map.values()))


        