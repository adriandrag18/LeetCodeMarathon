# title: Zigzag Conversion
# timestamp: 2025-06-09 00:41:14
# problemUrl: https://leetcode.com/problems/zigzag-conversion/
# memory: 18 MB
# runtime: 7 ms

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        rows = [[] for _ in range(numRows)]
        i = mod = 0
        for c in s:
            rows[i].append(c)
            if mod:
                i -= 1
                if i == 0:
                    mod = 1 - mod
            else:
                i += 1
                if i == numRows - 1:
                    mod = 1 - mod

        
        res = []
        for row in rows:
            res.extend(row)
        
        return ''.join(res)