# title: Plus One
# timestamp: 2025-05-23 00:33:41
# problemUrl: https://leetcode.com/problems/plus-one/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod((digits[i] + carry), 10)
        
        if carry == 1:
            return [1] + digits
        
        return digits