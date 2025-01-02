# title: Maximum Beauty of an Array After Applying Operation
# timestamp: 2025-01-02 12:57:43
# problemUrl: https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/
# memory: 29.9 MB
# runtime: 220 ms

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)
        l = 0
        start = nums[0] + k
        res = 1
        for r in range(1, len(nums)):
            while start < nums[r] - k:
                l += 1
                start = nums[l] + k
            res = max(res, r - l + 1)
            # print(l, r, res, nums[l:r])
        
        return res