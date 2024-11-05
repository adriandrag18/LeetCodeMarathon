# title: Permutation in String
# timestamp: 2024-11-05 22:39:18
# problemUrl: https://leetcode.com/problems/permutation-in-string/
# memory: 16.7 MB
# runtime: 11 ms

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq, cFreq = {}, {}
        for c1, c2 in zip(s1, s2):
            cFreq[c2] = cFreq.get(c2, 0) + 1
            freq[c1] = freq.get(c1, 0) + 1
        if freq == cFreq:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            cFreq[s2[l]] -= 1
            if cFreq[s2[l]] == 0:
                cFreq.pop(s2[l])
            l += 1
            cFreq[s2[r]] = cFreq.get(s2[r], 0) + 1
            if freq == cFreq:
                return True
        
        return False
