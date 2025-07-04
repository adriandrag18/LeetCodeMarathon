# title: Design Add and Search Words Data Structure
# timestamp: 2025-01-02 15:30:47
# problemUrl: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# memory: 65.7 MB
# runtime: 1185 ms

class WordDictionary:
    class TrieNode:
        def __init__(self, children = None, isEnd=False):
            self.children = children if children else {}
            self.isEnd = isEnd

        def __repr__(self):
            return f'({1 if self.isEnd else 0}{self.children})'
    
    def __init__(self):
        self.root = self.TrieNode()
    
    def addWord(self, word: str) -> None:
        n = self.root
        for c in word:
            if c not in n.children:
                n.children[c] = self.TrieNode()
            n = n.children[c]
        n.isEnd = True
    
    def search(self, word: str, root=None) -> bool:
        n = self.root if not root else root
        # print(word)
        for i, c in enumerate(word):
            # print(c, n)
            if c != '.':
                if c not in n.children:
                    return False
                n = n.children[c]
                continue
            
            rest = word[i+1:]
            for node in n.children.values():
                if self.search(rest, node):
                    return True

            return False
        
        return n.isEnd


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)