# title: Special Array I
# timestamp: 2025-02-01 22:46:26
# problemUrl: https://leetcode.com/problems/special-array-i/
# memory: 18 MB
# runtime: 3 ms

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        isOdd = (nums[0] % 2 == 1)
        for num in nums:
            if isOdd and (num % 2 == 0):
                return False
            if not isOdd and (num % 2 == 1):
                return False
            isOdd = not isOdd

        return True