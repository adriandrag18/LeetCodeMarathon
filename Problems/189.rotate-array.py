# title: Rotate Array
# timestamp: 2025-01-06 11:30:43
# problemUrl: https://leetcode.com/problems/rotate-array/
# memory: 25.8 MB
# runtime: 3 ms

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        left = nums[:n-k]
        right = nums[n-k:]
        
        nums.clear()
        nums.extend(right)
        nums.extend(left)