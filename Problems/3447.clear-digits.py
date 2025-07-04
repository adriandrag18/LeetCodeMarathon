# title: Clear Digits
# timestamp: 2025-02-10 14:26:55
# problemUrl: https://leetcode.com/problems/clear-digits/
# memory: 17.8 MB
# runtime: 5 ms

class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                if stack:
                    stack.pop()
                continue
            stack.append(c)
        
        return ''.join(stack)
            