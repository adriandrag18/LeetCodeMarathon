# title: Basic Calculator II
# timestamp: 2025-06-20 11:20:38
# problemUrl: https://leetcode.com/problems/basic-calculator-ii/
# memory: 21.6 MB
# runtime: 47 ms

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        def update(sign, num):
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                el = stack.pop()
                res = el // num
                if el < 0:
                    res = -((-el) // num)
                stack.append(res)
        
        num, sign = 0, '+'
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c in '+-*/':
                update(sign, num)
                num, sign = 0, c
        update(sign, num)
        
        return sum(stack)