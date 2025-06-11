# title: Permutations
# timestamp: 2024-12-28 00:13:40
# problemUrl: https://leetcode.com/problems/permutations/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def func(perm, rest):
            if not rest:
                res.append(perm)
                return
            
            el = rest.pop()
            
            for i in range(len(perm) + 1):
                p = perm[:]
                p.insert(i, el)
                func(p, rest)
            
            rest.append(el)
        
        res = []
        func([], nums)
        return res