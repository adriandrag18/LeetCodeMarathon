# title: Search Suggestions System
# timestamp: 2025-01-02 13:33:57
# problemUrl: https://leetcode.com/problems/search-suggestions-system/
# memory: 24.1 MB
# runtime: 926 ms

class Solution:    
    class Trie:
        class TrieNode:
            def __init__(self, children = None, isEnd=False):
                self.children = children if children else {}
                self.isEnd = isEnd
        
        def __init__(self):
            self.root = self.TrieNode()
        
        def insert(self, word):
            n = self.root
            for c in word:
                if c not in n.children:
                    n.children[c] = self.TrieNode({})
                n = n.children[c]
            n.isEnd = True
        
        def startsWith(self, prefix):
            n = self.root
            for c in prefix:
                if c not in n.children:
                    return []
                n = n.children[c]
            
            res = []
            if n.isEnd:
                res.append(prefix)
            res.extend([prefix + el for el in self.get(n)])
            return sorted(res)
        
        def get(self, node):
            if not node:
                return []
            
            res = []
            for c, n in node.children.items():
                if n.isEnd:
                    res.append(c)
                res.extend([c + el for el in self.get(n)])

            return res
            
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = self.Trie()
        for prod in products:
            trie.insert(prod)
        
        res = []
        for i in range(len(searchWord)):
            pred = trie.startsWith(searchWord[:i+1])
            res.append(pred[:3])
        
        return res
        