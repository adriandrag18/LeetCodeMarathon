# title: Subsets
# timestamp: 2024-12-27 23:45:51
# problemUrl: https://leetcode.com/problems/subsets/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def rec(li, i):
            if i == len(nums):
                self.res.append(li)
                return
            rec(li[:], i + 1)
            li.append(nums[i])
            rec(li, i + 1)

        rec([], 0)
        return self.res