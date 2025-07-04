# title: Basic Calculator
# timestamp: 2025-06-19 22:27:45
# problemUrl: https://leetcode.com/problems/basic-calculator/
# memory: 19 MB
# runtime: 47 ms

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i, n = 0, len(s)
        while i < n:
            num = 0
            if s[i].isdigit():
                num = s[i]
                while i + 1 < n and s[i+1].isdigit():
                    num += s[i+1]
                    i += 1
                num = int(num)
            elif s[i] in '+ ':
                i += 1
                continue
            elif s[i] in '-(':
                stack.append(s[i])
                i += 1
                continue
            elif s[i] == ')':
                num = stack.pop()
                while (el := stack.pop()) != '(':
                    num += el
            
            if stack and stack[-1] == '-':
                num = -num
                stack.pop()
            stack.append(num)
            
            i += 1

        return sum(stack)          