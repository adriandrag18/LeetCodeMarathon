# title: Find All Anagrams in a String
# timestamp: 2025-06-07 13:27:15
# problemUrl: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# memory: 18.8 MB
# runtime: 63 ms

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        res = []
        target, window = Counter(p), Counter(s[:len(p)])
        have, need = 0, len(target)
        for c, n in target.items():
            if c in window and window[c] == n:
                have += 1
        if have == need:
            res.append(0)
        j = len(p)
        for i in range(len(p), len(s)):
            if s[i - j] != s[i]:
                if s[i - j] in target and window[s[i - j]] == target[s[i - j]]:
                    have -= 1
                if s[i] in target and s[i] in window and window[s[i]] == target[s[i]]:
                    have -= 1

                window[s[i - j]] -= 1
                window[s[i]] = window.get(s[i], 0) + 1
                
                if s[i - j] in target and window[s[i - j]] == target[s[i - j]]:
                    have += 1
                if s[i] in target and window[s[i]] == target[s[i]]:
                    have += 1
            if have == need:
                res.append(i - j + 1)
        
        return res