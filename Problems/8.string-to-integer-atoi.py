# title: String to Integer (atoi)
# timestamp: 2024-12-28 02:02:30
# problemUrl: https://leetcode.com/problems/string-to-integer-atoi/
# memory: 17.7 MB
# runtime: 1 ms

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        res = 0
        started = False
        for c in s:
            if not started and c in ' \n\t':
                if started:
                    break
                continue
            if c == '-':
                if started:
                    break
                started = True
                sign = -1
                continue
            if c == '+':
                if started:
                    break
                started = True
                continue
            if not c.isdigit():
                break
            
            started = True
            res *= 10
            res += int(c)
            
            if -2 ** 31 > sign * res:
                res = 2 ** 31
                break
            if sign * res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
                break

        return sign * res