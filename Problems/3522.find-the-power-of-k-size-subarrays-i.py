# title: Find the Power of K-Size Subarrays I
# timestamp: 2024-11-16 14:10:28
# problemUrl: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
# memory: 16.8 MB
# runtime: 3 ms

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        res = [-1] * (len(nums) - k + 1)
        l, r = 0, 1
        while l <= len(nums) - k and r < len(nums):
            if r - l == k:
                res[l] = nums[r-1]
                l += 1
                continue
            
            if nums[r-1] + 1 == nums[r]:
                r += 1
                continue
            
            l = r
            r += 1

        if r - l == k:
            res[l] = nums[r-1]

        return res