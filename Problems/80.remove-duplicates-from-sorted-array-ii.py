# title: Remove Duplicates from Sorted Array II
# timestamp: 2025-01-05 00:24:22
# problemUrl: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# memory: 18 MB
# runtime: 54 ms

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        removed = 0
        for i, num in enumerate(nums):
            if i < 2:
                continue
            if num == nums[i - 1 - removed] and nums[i - 1 - removed] == nums[i - 2 - removed]:
                removed += 1
                continue
            nums[i - removed] = num
        
        return len(nums) - removed