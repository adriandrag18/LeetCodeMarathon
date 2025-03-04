# title: Check if Number is a Sum of Powers of Three
# timestamp: 2025-03-04 11:03:11
# problemUrl: https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 0:
                n //= 3
            elif n % 3 == 1:
                n -= 1
            else:
                return False
        
        return True