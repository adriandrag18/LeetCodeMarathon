# title: Valid Triangle Number
# timestamp: 2025-06-25 00:42:44
# problemUrl: https://leetcode.com/problems/valid-triangle-number/
# memory: 17.8 MB
# runtime: 4768 ms

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                sum = nums[i] + nums[j]
                index = bisect_left(nums[j+1:], sum)
                count += index

        return count