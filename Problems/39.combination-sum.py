# title: Combination Sum
# timestamp: 2024-12-28 00:06:23
# problemUrl: https://leetcode.com/problems/combination-sum/
# memory: 17.9 MB
# runtime: 6 ms

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(t, r, start):
            if t == 0:
                result.append(r)
                return
            if t < 0:
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= t:
                    new = r.copy()
                    new.append(candidates[i])
                    helper(t - candidates[i], new, i)
                    
        result = []
        helper(target, [], 0)
        return result