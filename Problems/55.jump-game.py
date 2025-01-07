# title: Jump Game
# timestamp: 2025-01-07 22:40:01
# problemUrl: https://leetcode.com/problems/jump-game/
# memory: 18.9 MB
# runtime: 13 ms

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last:
                last = i
                # print(last)
        
        return last == 0