# title: Single Number II
# timestamp: 2025-06-13 11:41:40
# problemUrl: https://leetcode.com/problems/single-number-ii/
# memory: 19.3 MB
# runtime: 54 ms

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        for num in nums:
            sign = 1
            if num < 0:
                sign = -1
                num = -num - 1
            binNum = bin(num)[:1:-1]
            if sign == -1:
                bits[-1] += 1
            for i in range(len(binNum)):
                bits[i] += sign * int(binNum[i])
        sign = bits[-1] % 3
        bits[-1] = 0
        num = int(''.join(['1' if bit % 3 else '0' for bit in reversed(bits)]), 2)
        if not sign:
            return num
        return -num - 1