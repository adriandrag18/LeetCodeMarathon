# title: Valid Parentheses
# timestamp: 2024-11-03 16:06:46
# problemUrl: https://leetcode.com/problems/valid-parentheses/
# memory: 16.8 MB
# runtime: 3 ms

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'[': ']', '{': '}', '(': ')'}
        for c in s:
            if c in map:
                stack.append(c)
                # print(stack)
                continue
            if len(stack) == 0 or c != map[stack.pop()]:
                # print(stack)
                return False

        # print(stack)
        return len(stack) == 0