# title: Longest Increasing Subsequence
# timestamp: 2025-05-24 14:29:32
# problemUrl: https://leetcode.com/problems/longest-increasing-subsequence/
# memory: 18 MB
# runtime: 7 ms

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # def rec(i):
        #     if dp[i] != -1: return dp[i]
            
        #     res = 0
        #     for j in range(i + 1, len(nums)):
        #         if i >= 0 and nums[j] <= nums[i]:
        #             continue
        #         res = max(res, rec(j) + 1)
                    
        #     if i != -1: dp[i] = res
        #     return res
        
        # dp = [-1] * len(nums)
        # return rec(-1)

        # n = len(nums)
        # dp = [-1] * n
        # dp[-1] = 1
        # for i in range(n-2, -1, -1):
        #     dp[i] = 1
        #     for j in range(n - 1, -1, -1):
        #         if nums[i] >= nums[j]:
        #             continue
        #         dp[i] = max(dp[i], dp[j] + 1)
        
        # return max(dp)

        def binSearch(target):
            nonlocal li
            l, r = 0, len(li) - 1
            while l <= r:
                m = (l + r) // 2
                if li[m] == target:
                    return m
                elif li[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return l
        
        li = [nums[0]]
        for num in nums[1:]:
            if num > li[-1]:
                li.append(num)
                continue
            li[binSearch(num)] = num
        
        return len(li)