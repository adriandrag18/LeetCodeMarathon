# title: Shortest Subarray With OR at Least K II
# timestamp: 2024-11-10 22:03:49
# problemUrl: https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/
# memory: 35.7 MB
# runtime: 42 ms

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if max(nums) >= k:
            return 1
        
        l, res, curr = 0, len(nums) + 1, nums[0]
        for r in range(1, len(nums)):
            if curr < k:
                curr |= nums[r]
            
            if curr < k:
                continue
            res = min(res, r - l + 1)

            l, curr = r, nums[r]
            while (curr | nums[l-1]) < k:
                l -= 1
                curr |= nums[l]
            res = min(res, r - l + 2)


        return res if res <= len(nums) else -1