# title: Simplify Path
# timestamp: 2025-06-19 21:52:50
# problemUrl: https://leetcode.com/problems/simplify-path/
# memory: 17.8 MB
# runtime: 0 ms

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for el in path:
            if not el:
                continue
            elif el == '.':
                continue
            elif el == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(el)
        
        return  '/' + '/'.join(stack)