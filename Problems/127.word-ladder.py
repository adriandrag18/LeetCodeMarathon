# title: Word Ladder
# timestamp: 2025-05-20 15:01:58
# problemUrl: https://leetcode.com/problems/word-ladder/
# memory: 18.9 MB
# runtime: 240 ms

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordMap = {w: float('inf') for w in wordList}
        wordMap[beginWord] = 1

        if endWord not in wordList:
            return 0
        
        def diff(word1):
            return sum([1 for a, b in zip(word1, endWord) if a != b])
        
        def neighbors(word):
            chars = [c for c in word]
            res = []
            for i in range(len(chars)):
                for j in range(26):
                    char = chr(j + 97)
                    if char == word[i]:
                        continue
                    chars[i] = char
                    s = ''.join(chars)
                    if s in wordMap:
                        res.append(s)
                chars[i] = word[i]
            return res

        visited = set()
        heap = []
        heappush(heap, (diff(beginWord), beginWord))

        while heap:
            _, node = heappop(heap)
            
            if node == endWord:
                break
            if node in visited:
                continue
            visited.add(node)
            cost = wordMap[node] + 1
            for neighbor in neighbors(node):
                if neighbor in visited:
                    continue
                if wordMap[neighbor] > cost:
                    wordMap[neighbor] = cost
                    heappush(heap, (diff(neighbor) + cost, neighbor))
        
        return wordMap[endWord] if wordMap[endWord] != float('inf') else 0