# title: Apply Operations to an Array
# timestamp: 2025-03-01 17:35:39
# problemUrl: https://leetcode.com/problems/apply-operations-to-an-array/
# memory: 17.9 MB
# runtime: 19 ms

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        n = len(nums)
        while 0 in nums:
            nums.remove(0)  
        nums.extend([0] * (n - len(nums)))
        return nums