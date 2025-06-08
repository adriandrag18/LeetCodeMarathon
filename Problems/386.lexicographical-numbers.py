# title: Lexicographical Numbers
# timestamp: 2025-06-08 03:10:34
# problemUrl: https://leetcode.com/problems/lexicographical-numbers/
# memory: 22.8 MB
# runtime: 23 ms

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(num):
            if num <= n:
                nonlocal res
                res.append(num)
            else:
                return True
            num *= 10
            for i in range(10):
                if dfs(num + i):
                    break
        
        for i in range(1, 10):
            dfs(i)
        
        return res