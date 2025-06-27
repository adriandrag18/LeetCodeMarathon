# title: Longest Subsequence Repeated k Times
# timestamp: 2025-06-27 11:50:33
# problemUrl: https://leetcode.com/problems/longest-subsequence-repeated-k-times/
# memory: 18.2 MB
# runtime: 896 ms

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        res = ''
        letters = []
        for c, count in Counter(s).items():
            if count >= k:
                res = max(res, c)
                letters.extend([c] * (count // k))

        if not res:
            return ''
        
        def func(curr, letters):
            nonlocal res
            if len(curr) > len(res) or (len(curr) == len(res) and curr > res):
                res = curr
                
            for i, c in enumerate(letters):
                if letters[i] == '#':
                    continue
                
                next = curr + c
                it = iter(s)
                if all(c in it for c in next * k):
                    letters[i] = '#'
                    func(next, letters)
                    letters[i] = c

        func('', letters)
        return res