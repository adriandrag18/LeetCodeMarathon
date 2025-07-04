# title: Next Permutation
# timestamp: 2025-06-09 12:16:48
# problemUrl: https://leetcode.com/problems/next-permutation/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        i = n-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i == -1:
            nums.reverse()
            return

        j = i + 1
        while j < n - 1:
            if nums[i] >= nums[j + 1]:
                break
            j += 1
        
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = sorted(nums[i+1:])
        