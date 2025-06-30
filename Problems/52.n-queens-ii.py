# title: N-Queens II
# timestamp: 2025-06-19 22:49:51
# problemUrl: https://leetcode.com/problems/n-queens-ii/
# memory: 17.9 MB
# runtime: 8 ms

class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(l, cols, diag1, diag2):
            if len(l) == n:
                nonlocal res
                res += 1

            row = len(l)
            for pos in range(n):
                if pos in cols or row - pos in diag1 or row + pos in diag2:
                    continue
                
                l.append(pos)
                cols.add(pos)
                diag1.add(row - pos)
                diag2.add(row + pos)
                
                helper(l, cols, diag1, diag2)
                
                l.pop()
                cols.remove(pos)
                diag1.remove(row - pos)
                diag2.remove(row + pos)

        res = 0
        helper([], set(), set(), set())
        return res