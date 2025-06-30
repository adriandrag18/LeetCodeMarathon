# title: Adjacent Increasing Subarrays Detection I
# timestamp: 2024-11-16 14:36:14
# problemUrl: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/
# memory: 16.6 MB
# runtime: 79 ms

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1: return True

        l, r = 0, 1
        while l <= len(nums) - 2 * k:
            # print(l, r)
            if r - l == k:
                i = r
                # print("k")
                while i < r + k - 1 and nums[i] < nums[i+1]: 
                    i += 1
                if i == r + k - 1:
                    return True
                l = i + 1 - k
                r = l + 1
                continue
                
            if l == r or nums[r - 1] < nums[r]:
                # print("add")
                r += 1
                continue
            
            l = r
            r += 1

        return False