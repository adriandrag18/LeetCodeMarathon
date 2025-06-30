# title: 3Sum Closest
# timestamp: 2025-01-09 15:52:52
# problemUrl: https://leetcode.com/problems/3sum-closest/
# memory: 17.8 MB
# runtime: 259 ms

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 10**5
        for i in range(0, len(nums) - 2):
            if nums[i] + nums[i+1] + nums[i+2] - target > abs(res - target):
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[j] + nums[k] + nums[i]
                if s == target:
                    return s
                if abs(res - target) > abs(s - target):
                    res = s
                
                if s < target:
                    j += 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1
                    continue
                k -= 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
        
        return res