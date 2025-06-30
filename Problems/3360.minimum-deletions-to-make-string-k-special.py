# title: Minimum Deletions to Make String K-Special
# timestamp: 2025-06-21 16:31:12
# problemUrl: https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/
# memory: 18 MB
# runtime: 51 ms

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        res = n = len(word)
        freq = sorted(Counter(word).values())
        m = len(freq)
        
        if len(freq) == 1:
            return 0
        
        r = 1
        prefix, suffix = 0, n - freq[0]
        for l in range(m):
            while r < m and freq[r] - freq[l] <= k:
                suffix -= freq[r]
                r += 1
            removed = prefix + suffix - (freq[l] + k) * (m - r)
            res = min(res, removed)
            prefix += freq[l]
        
        return res
