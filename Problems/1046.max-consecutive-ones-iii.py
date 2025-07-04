# title: Max Consecutive Ones III
# timestamp: 2024-12-28 20:15:36
# problemUrl: https://leetcode.com/problems/max-consecutive-ones-iii/
# memory: 18.5 MB
# runtime: 47 ms

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        count = k
        l = 0
        for r in range(len(nums)):
            # print(l, r, count, res)
            if nums[r]:
                res = max(res, r-l+1)
                continue
            count -= 1
            if count >= 0:
                res = max(res, r-l+1)
                continue
            
            while nums[l]: 
                l += 1
            l += 1
            count += 1
        # print(l, r, count, res)

        return res