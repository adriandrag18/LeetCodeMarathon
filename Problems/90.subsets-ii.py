# title: Subsets II
# timestamp: 2024-12-28 00:21:21
# problemUrl: https://leetcode.com/problems/subsets-ii/
# memory: 18.3 MB
# runtime: 0 ms

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def rec(li, i):
            if i == len(nums):
                res.add(tuple(sorted(li)))
                return
            rec(li, i + 1)
            li.append(nums[i])
            rec(li, i + 1)
            li.pop()

        res = set()
        rec([], 0)
        return [[e for e in el] for el in res]    