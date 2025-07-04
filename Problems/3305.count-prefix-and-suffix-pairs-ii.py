# title: Count Prefix and Suffix Pairs II
# timestamp: 2025-01-09 15:18:02
# problemUrl: https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/
# memory: 210.6 MB
# runtime: 1303 ms

class Solution:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.count = 0
            
        def __init__(self):
            self.root = self.TrieNode()

        def insert(self, word):
            res, current = 0, self.root
            for el in zip(word, word[::-1]):
                if el not in current.children:
                    current.children[el] = self.TrieNode()
                current = current.children[el]
                res += current.count
            
            current.count += 1
            return res

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        trie = self.Trie()
        for word in words:
            res += trie.insert(word)
        
        return res