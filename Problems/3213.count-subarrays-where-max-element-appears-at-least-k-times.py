# title: Count Subarrays Where Max Element Appears at Least K Times
# timestamp: 2025-04-29 17:39:58
# problemUrl: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# memory: 29.6 MB
# runtime: 76 ms

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        count, res = 0, 0
        l = 0
        
        for r in range(len(nums)):
            if nums[r] == target:
                count += 1
                if count >= k:
                    inital = l
                    while nums[l] != target:
                        l += 1
                    l += 1
                    count -= 1
                    res += (l - inital) * (len(nums) - r)
        
        return res
