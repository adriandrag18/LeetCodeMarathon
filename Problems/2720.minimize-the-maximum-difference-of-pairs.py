# title: Minimize the Maximum Difference of Pairs
# timestamp: 2025-06-14 00:06:31
# problemUrl: https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
# memory: 32.6 MB
# runtime: 312 ms

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        # bin search between 0 and max possible diff
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            i = 1
            count = 0
            while i < n:
                if nums[i] - nums[i-1] <= m:
                    count += 1
                    i += 1
                i += 1
            if count >= p:
                r = m
            else:
                l = m + 1
        
        return r