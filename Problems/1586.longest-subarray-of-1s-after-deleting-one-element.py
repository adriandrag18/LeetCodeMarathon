# title: Longest Subarray of 1's After Deleting One Element
# timestamp: 2024-12-30 11:44:01
# problemUrl: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# memory: 21.8 MB
# runtime: 49 ms

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        deleted = False
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                res = max(res, r - l + 1 - (1 if deleted else 0))
                continue
            if not deleted:
                deleted = True
                continue
            while nums[l] and l <= r:
                l += 1
            l += 1
        
        return res - (1 if not deleted else 0)