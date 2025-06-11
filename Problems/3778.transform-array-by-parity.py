# title: Transform Array by Parity
# timestamp: 2025-03-01 16:38:51
# problemUrl: https://leetcode.com/problems/transform-array-by-parity/
# memory: 17.9 MB
# runtime: 5 ms

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        nums = [0 if num % 2 == 0 else 1 for num in nums]
        print(nums)
        nums.sort()
        print(nums)
        return nums