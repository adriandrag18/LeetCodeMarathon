# title: House Robber IV
# timestamp: 2025-03-15 16:16:14
# problemUrl: https://leetcode.com/problems/house-robber-iv/
# memory: 28.7 MB
# runtime: 247 ms

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        n = len(nums)


        def helper(m):
            taken = False
            count = 0
            for i in range(n):
                if taken:
                    taken = False
                elif nums[i] <= m:
                    count += 1
                    taken = True

            return count >= k
        
        l, r = min(nums), max(nums)
        while l <= r:
            m = (l + r) // 2
            if helper(m):
                r = m - 1
            else:
                l = m + 1
        
        return r + 1
