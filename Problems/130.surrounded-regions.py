# title: Surrounded Regions
# timestamp: 2025-06-05 13:38:12
# problemUrl: https://leetcode.com/problems/surrounded-regions/
# memory: 42.9 MB
# runtime: 85 ms

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        def find(node) -> bool:
            x, y = node
            surr = 0 < x < n - 1 and 0 < y < m - 1
            board[x][y] = '#'
            for nx, ny in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'O':
                    surr = find((nx, ny)) and surr
            return surr

        def capture(node):
            x, y = node
            board[x][y] = 'X'
            for nx, ny in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '#':
                    capture((nx, ny))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    if find((i, j)):
                        capture((i, j))

        for i in range(n):
            for j in range(m):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                        

        