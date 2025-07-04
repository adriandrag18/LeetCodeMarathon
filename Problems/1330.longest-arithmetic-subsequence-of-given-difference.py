# title: Longest Arithmetic Subsequence of Given Difference
# timestamp: 2025-06-30 00:58:23
# problemUrl: https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
# memory: 28.8 MB
# runtime: 95 ms

class Solution:
    def longestSubsequence(self, arr: List[int], dif: int) -> int:
        map = {}
        res = 1
        for el in arr:
            map[el + dif] = map.get(el, 0) + 1
            res = max(res, map[el + dif])
        
        return res