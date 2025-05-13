# title: Evaluate Reverse Polish Notation
# timestamp: 2025-05-13 15:01:02
# problemUrl: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# memory: 19.3 MB
# runtime: 0 ms

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                stack.append(-stack.pop() + stack.pop())
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                b = stack.pop()
                stack.append(int(stack.pop() / b))
            else:
                stack.append(int(t))
        
        return stack[0]