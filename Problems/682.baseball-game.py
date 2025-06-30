# title: Baseball Game
# timestamp: 2025-06-12 22:12:17
# problemUrl: https://leetcode.com/problems/baseball-game/
# memory: 17.9 MB
# runtime: 0 ms

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)