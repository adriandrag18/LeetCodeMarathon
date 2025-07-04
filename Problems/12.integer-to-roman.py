# title: Integer to Roman
# timestamp: 2025-01-07 22:31:17
# problemUrl: https://leetcode.com/problems/integer-to-roman/
# memory: 17.5 MB
# runtime: 11 ms

class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        symbols =  ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for symbol, n in zip(symbols, nums):
            res.append(symbol * (num // n))
            num %= n
        
        return ''.join(res)