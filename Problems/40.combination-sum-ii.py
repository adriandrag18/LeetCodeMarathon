# title: Combination Sum II
# timestamp: 2024-12-28 01:22:23
# problemUrl: https://leetcode.com/problems/combination-sum-ii/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(target, start, li, isPicked):
            # print('\t' * start, li, start)
            if target == 0:
                res.append(li[:])
                return
            if target < 0 or start >= len(candidates):
                return
            if target < candidates[start]:
                return
            
            func(target, start + 1, li, False)
            
            # print('\t' * start, start, candidates[start - 1], candidates[start], candidates[start - 1] == candidates[start], isPicked)
            if start > 0 and candidates[start - 1] == candidates[start] and not isPicked:
                return
            
            li.append(candidates[start])
            func(target - candidates[start], start + 1, li, True)
            li.pop()
        
        candidates.sort()
        res = []
        func(target, 0, [], False)
        return res