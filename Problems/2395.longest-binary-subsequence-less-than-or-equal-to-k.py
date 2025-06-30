# title: Longest Binary Subsequence Less Than or Equal to K
# timestamp: 2025-06-27 00:57:58
# problemUrl: https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
# memory: 17.8 MB
# runtime: 4 ms

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        curr = count = 0
        for i, c in enumerate(s[::-1]):
            if c == '0':
                count += 1
                continue
            if curr + (1 << i) <= k:
                count += 1
                curr += 1 << i
           
        return count
