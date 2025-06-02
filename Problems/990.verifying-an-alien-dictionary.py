# title: Verifying an Alien Dictionary
# timestamp: 2025-06-02 12:45:26
# problemUrl: https://leetcode.com/problems/verifying-an-alien-dictionary/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map = {}
        for i, char in enumerate(order):
            map[char] = i
        
        def smaller(a, b):
            for x, y in zip(a, b):
                if map[x] < map[y]:
                    return True
                if map[x] > map[y]:
                    return False
            
            return len(a) <= len(b)
        
        for i in range(len(words) - 1):
            if not smaller(words[i], words[i + 1]):
                return False
        
        return True