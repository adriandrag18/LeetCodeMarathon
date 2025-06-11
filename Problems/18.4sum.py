# title: 4Sum
# timestamp: 2025-01-09 16:46:45
# problemUrl: https://leetcode.com/problems/4sum/
# memory: 17.9 MB
# runtime: 167 ms

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(n, first) -> List[List[int]]:
            t = target - first
            res = []
            for i in range(n, len(nums) - 2):
                # print(i, '3')
                if 3 * nums[i] > t:
                    break
                if i > n and nums[i-1] == nums[i]:
                    continue
                j, k = i + 1, len(nums) - 1
                while j < k:
                    s = nums[j] + nums[k] + nums[i]
                    if s == t:
                        res.append([first, nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while nums[j-1] == nums[j] and j < k:
                            j += 1
                        while nums[k+1] == nums[k] and j < k:
                            k -= 1
                        continue
                    if s < t:
                        j += 1
                        continue    
                    k -= 1
            return res
        
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            # print(i, '4')
            if 4 * nums[i] > target:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            res.extend(threeSum(i + 1, nums[i]))
        
        return res
