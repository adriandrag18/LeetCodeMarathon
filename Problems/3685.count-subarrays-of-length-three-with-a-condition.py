# title: Count Subarrays of Length Three With a Condition
# timestamp: 2024-12-21 16:33:31
# problemUrl: https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/
# memory: 18 MB
# runtime: 16 ms

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i + 1] % 2 == 0 and nums[i] + nums[i + 2] == nums[i + 1] / 2:
                res += 1
        
        return res