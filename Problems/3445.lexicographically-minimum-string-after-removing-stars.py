# title: Lexicographically Minimum String After Removing Stars
# timestamp: 2025-06-07 13:09:41
# problemUrl: https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
# memory: 29.1 MB
# runtime: 555 ms

class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        for i, c in enumerate(s):
            if c == '*':
                heappop(heap)
            else:
                heappush(heap, (c, -i))
        
        res = [''] * len(s)
        for c, i in heap:
            res[-i] = c

        return ''.join(res)