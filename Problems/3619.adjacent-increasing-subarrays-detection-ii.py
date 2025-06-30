# title: Adjacent Increasing Subarrays Detection II
# timestamp: 2024-11-16 14:53:53
# problemUrl: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/
# memory: 44.5 MB
# runtime: 2812 ms

class Solution:
   def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        def hasIncreasingSubarrays(k: int) -> bool:
            if k == 1: return True
    
            l, r = 0, 1
            while l <= len(nums) - 2 * k:
                if r - l == k:
                    i = r
                    while i < r + k - 1 and nums[i] < nums[i+1]: 
                        i += 1
                    if i == r + k - 1:
                        return True
                    l = i + 1 - k
                    r = l + 1
                    continue
                    
                if l == r or nums[r - 1] < nums[r]:
                    r += 1
                    continue
                
                l = r
                r += 1
    
            return False
        
        l, r = 2, len(nums) // 2
        res = 1
        while l <= r:
            mid = (l + r) // 2
            if hasIncreasingSubarrays(mid):
                res = max(res, mid)
                l = mid + 1
                continue
            r = mid - 1
            
        return res