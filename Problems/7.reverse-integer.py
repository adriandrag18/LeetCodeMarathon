# title: Reverse Integer
# timestamp: 2025-05-20 11:46:43
# problemUrl: https://leetcode.com/problems/reverse-integer/
# memory: 17.6 MB
# runtime: 39 ms

class Solution:
    def reverse(self, x: int) -> int:
        threashold = 214748364
        out = 0
        sign = -1 if x < 0 else 1
        x *= sign
        while x:
            out *= 10
            out += x % 10
            x //= 10

            if x != 0 and (out > threashold or out < -threashold):
                return 0
        
        return out * sign