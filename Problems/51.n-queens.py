# title: N-Queens
# timestamp: 2025-01-10 14:51:04
# problemUrl: https://leetcode.com/problems/n-queens/
# memory: 18.2 MB
# runtime: 8 ms

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def convertToBoard(l):
            return ['.' * pos + 'Q' + '.' * (n - pos - 1) for pos in l]
                
        def helper(l, cols, diag1, diag2):
            if len(l) == n:
                res.append(convertToBoard(l))

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

        res = []
        helper([], set(), set(), set())
        return res