# title: 3Sum
# timestamp: 2024-11-01 23:02:30
# problemUrl: https://leetcode.com/problems/3sum/
# memory: 19.7 MB
# runtime: 577 ms

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k < len(nums):
                s = nums[j] + nums[k] + nums[i]
                if s == 0:
                    # if [nums[i], nums[j], nums[k]] not in res:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j-1] == nums[j] and j < k:
                        j += 1
                    while nums[k+1] == nums[k] and j < k:
                        k -= 1
                    continue
                if s < 0:
                    j += 1
                    continue    
                k -= 1
            # seen = set()
            # for el in nums[i+1:]:
            #     if (-nums[i] - el) in seen and [nums[i], -nums[i] - el, el] not in res:
            #         res.append([nums[i], -nums[i] - el, el])
            #     seen.add(el)
        return res
            