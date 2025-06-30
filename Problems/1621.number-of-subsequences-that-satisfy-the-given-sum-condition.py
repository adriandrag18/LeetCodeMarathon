# title: Number of Subsequences That Satisfy the Given Sum Condition
# timestamp: 2025-06-29 07:45:16
# problemUrl: https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
# memory: 28.3 MB
# runtime: 251 ms

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        j = n - 1
        for i in range(n):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i > j:
                break
            res += 1 << (j - i)

        return res % (10**9 + 7)