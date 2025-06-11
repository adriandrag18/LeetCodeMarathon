# title: Decode String
# timestamp: 2024-12-30 12:37:59
# problemUrl: https://leetcode.com/problems/decode-string/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
                continue
            if num:
                stack.append(num)
                num = 0
            if c == '[':
                continue
            
            if c.isalpha():
                if stack and type(stack[-1]) == list:
                    stack[-1].append(c)
                    continue
                stack.append([c])
                continue
                
            decodedChars = stack.pop() * stack.pop()
            if stack and type(stack[-1]) == list:
                decodedChars = stack.pop() + decodedChars
            
            stack.append(decodedChars)

        return ''.join(stack[0])