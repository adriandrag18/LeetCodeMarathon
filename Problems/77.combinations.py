# title: Combinations
# timestamp: 2025-06-19 23:00:39
# problemUrl: https://leetcode.com/problems/combinations/
# memory: 59.6 MB
# runtime: 131 ms

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(start, l):
            if len(l) == k:
                nonlocal res
                res.append(l[:])
                return
            
            for i in range(start, n + 1):
                l.append(i)
                helper(i + 1, l)
                l.pop()
            
        res = []
        helper(1, [])
        return res