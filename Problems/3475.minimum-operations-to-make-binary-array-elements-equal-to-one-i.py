# title: Minimum Operations to Make Binary Array Elements Equal to One I
# timestamp: 2025-03-19 23:13:03
# problemUrl: https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/
# memory: 21.5 MB
# runtime: 146 ms

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n-2):
            if not nums[i]:
                for j in range(i, i + 3):
                    nums[j] = 0 if nums[j] else 1
                count += 1
        
        ones = nums.count(1)
        if ones == n:
            return count
        return -1