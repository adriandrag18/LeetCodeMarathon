# title: Word Search II
# timestamp: 2025-01-02 16:53:10
# problemUrl: https://leetcode.com/problems/word-search-ii/
# memory: 20.8 MB
# runtime: 7325 ms

class Solution:
    class Trie:
        class TrieNode:
            def __init__(self, children = None, isEnd=False):
                self.children = children if children else [None] * 27
                self.word = ''
        
        def __init__(self):
            self.root = self.TrieNode()
        
        def insert(self, word):
            n = self.root
            for c in word:
                c = ord(c) - ord('a')
                if not n.children[c]:
                    n.children[c] = self.TrieNode({})
                n = n.children[c]
            n.word = word
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.Trie()
        for word in words:
            trie.insert(word[:144]) 
        
        def dfs(position, node):
            i, j = position
            c = ord(board[i][j]) - ord('a')
            if not node.children[c]:
                return
            
            node = node.children[c]
            if node.word:
                res.append(node.word)
                node.word = ''
            
            board[i][j] = chr(ord('z') + 1)
            for k, l in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0 <= k < m and 0 <= l < n:
                    dfs((k, l), node)
            board[i][j] = chr(c + ord('a'))
        
        res = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                dfs((i, j), trie.root)
        
        return list(res)