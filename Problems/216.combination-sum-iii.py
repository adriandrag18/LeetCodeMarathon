# title: Combination Sum III
# timestamp: 2024-12-28 20:25:38
# problemUrl: https://leetcode.com/problems/combination-sum-iii/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k * (k + 1) / 2:
            return []
        
        def rec(start, li):
            if sum(li) == n and len(li) == k:
                res.append(li[:])
                return
            if sum(li) + start > n or len(li) >= k:
                return
            
            for i in range(start, 10):
                li.append(i)
                rec(i + 1, li)
                li.pop()

        res = []
        rec(1, [])
        return res