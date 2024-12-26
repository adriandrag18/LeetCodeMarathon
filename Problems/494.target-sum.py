# title: Target Sum
# timestamp: 2024-12-26 16:27:16
# problemUrl: https://leetcode.com/problems/target-sum/
# memory: 18.1 MB
# runtime: 86 ms

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # def rec(i, curr, s):
        #     if curr + s < target or curr - s > target:
        #         return 0
        #     if i == len(nums):
        #         if curr == target:
        #             return 1
        #         return 0
        #     return rec(i + 1, curr + nums[i], s - nums[i]) + rec(i + 1, curr - nums[i], s - nums[i])
            
        # s = sum(nums)
        # return rec(0, 0, s)

        old, map = {0: 1}, {}
        for i in range(len(nums) - 1, -1, -1):
            for el, num in old.items():
                map[el + nums[i]] = map.get(el + nums[i], 0) + num
                map[el - nums[i]] = map.get(el - nums[i], 0) + num
            old, map = map, {}
        
        return old[target] if target in old else 0
        