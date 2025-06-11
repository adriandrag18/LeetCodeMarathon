# title: String Matching in an Array
# timestamp: 2025-01-07 11:19:25
# problemUrl: https://leetcode.com/problems/string-matching-in-an-array/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda s: len(s))
        res = []
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        
        return res