# title: Counting Bits
# timestamp: 2025-05-20 11:19:34
# problemUrl: https://leetcode.com/problems/counting-bits/
# memory: 18.5 MB
# runtime: 3 ms

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        for i in range(1, n + 1):
            res.append(res[i // 2] + (i & 1))
        
        return res