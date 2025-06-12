# title: Largest Perimeter Triangle
# timestamp: 2025-06-12 20:54:54
# problemUrl: https://leetcode.com/problems/largest-perimeter-triangle/
# memory: 18.7 MB
# runtime: 11 ms

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i + 2] < nums[i + 1] + nums[i]:
                return nums[i + 2] + nums[i + 1] + nums[i]
        
        return 0

