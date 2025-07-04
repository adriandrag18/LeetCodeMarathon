# title: Minimize XOR
# timestamp: 2025-01-15 11:30:32
# problemUrl: https://leetcode.com/problems/minimize-xor/
# memory: 18 MB
# runtime: 0 ms

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count = bin(num2).count('1')
        num = bin(num1)[2:]
        res = 0
        for digit in num:
            res <<= 1
            if count and digit == '1' :
                res += 1
                count -= 1
        
        num = num[::-1]
        i, pow = 0, 1
        while count:
            if  i >= len(num) or num[i] == '0':
                res += pow
                count -= 1
            pow <<= 1
            i += 1

        return res