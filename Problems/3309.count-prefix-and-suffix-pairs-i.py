# title: Count Prefix and Suffix Pairs I
# timestamp: 2025-01-08 13:23:40
# problemUrl: https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/
# memory: 17.6 MB
# runtime: 3 ms

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i, word in enumerate(words):
            for word2 in words[i+1:]:
                # print(i, word, word2, res)
                if len(word) <= len(word2) and word == word2[:len(word)] and word == word2[-len(word):]:
                    res += 1
        
        return res