# title: Ransom Note
# timestamp: 2025-01-13 18:59:53
# problemUrl: https://leetcode.com/problems/ransom-note/
# memory: 17.9 MB
# runtime: 15 ms

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = Counter(magazine)
        for l, c in Counter(ransomNote).items():
            if c > letters.get(l, 0):
                return False
        
        return True