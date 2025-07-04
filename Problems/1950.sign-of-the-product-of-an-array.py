# title: Sign of the Product of an Array
# timestamp: 2025-06-12 20:21:29
# problemUrl: https://leetcode.com/problems/sign-of-the-product-of-an-array/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negCount = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                negCount += 1
        
        return -1 if negCount % 2 == 1 else 1