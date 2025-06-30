// title: Implement Trie (Prefix Tree)
// timestamp: 2024-04-17 20:42:46
// problemUrl: https://leetcode.com/problems/implement-trie-prefix-tree/
// memory: 12.6 MB
// runtime: 69 ms

type TrieNode struct {
    children map[rune]*TrieNode
    isEnd    bool
}

type Trie struct {
    root *TrieNode
}

func Constructor() Trie {
    return Trie{root: &TrieNode{children: make(map[rune]*TrieNode)}}
}

func (t *Trie) Insert(word string) {
    node := t.root
    for _, ch := range word {
        if _, ok := node.children[ch]; !ok {
            node.children[ch] = &TrieNode{children: make(map[rune]*TrieNode)}
        }
        node = node.children[ch]
    }
    node.isEnd = true
}

func (t *Trie) Search(word string) bool {
    node := t.root
    for _, ch := range word {
        if _, ok := node.children[ch]; !ok {
            return false
        }
        node = node.children[ch]
    }
    return node.isEnd
}

// StartsWith searches for a prefix in the Trie
func (t *Trie) StartsWith(prefix string) bool {
    node := t.root
    for _, ch := range prefix {
        if _, ok := node.children[ch]; !ok {
            return false
        }
        node = node.children[ch]
    }
    return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */