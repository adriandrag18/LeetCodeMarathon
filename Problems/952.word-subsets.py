# title: Word Subsets
# timestamp: 2025-01-10 04:44:57
# problemUrl: https://leetcode.com/problems/word-subsets/
# memory: 27 MB
# runtime: 455 ms

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wordsCounter2 = [Counter(word) for word in words2]
        map = {}
        for i in range(26):
            char = chr(i + ord('a'))
            m = max([wordCounter.get(char, 0) for wordCounter in wordsCounter2])
            if m:
                map[char] = m
        
        res = []
        for word in words1:
            counter = Counter(word)
            for char, count in map.items():
                if counter[char] < count:
                    break
            else:
                res.append(word)
        
        return res
            
