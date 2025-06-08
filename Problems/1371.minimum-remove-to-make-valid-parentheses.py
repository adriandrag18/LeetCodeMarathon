# title: Minimum Remove to Make Valid Parentheses
# timestamp: 2025-06-09 01:01:14
# problemUrl: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# memory: 19.5 MB
# runtime: 43 ms

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove = set()
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        for i in stack:
            remove.add(i)
        
        return ''.join([c for i, c in enumerate(s) if i not in remove])
