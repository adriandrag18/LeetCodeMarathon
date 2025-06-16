# title: Game of Life
# timestamp: 2025-06-16 17:52:01
# problemUrl: https://leetcode.com/problems/game-of-life/
# memory: 17.9 MB
# runtime: 3 ms

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        prev = [0] * n
        for i in range(m):
            curr = board[i].copy()
            for j in range(n):
                nei = prev[max(0, j-1):j+2]
                nei.extend([curr[j-1] if j > 0 else 0, curr[j+1] if j < n - 1 else 0])
                if i < m - 1:
                    nei.extend(board[i+1][max(0, j-1):j+2])

                count = sum(nei)
                board[i][j] = 1 if (curr[j] and count in [2, 3]) or (count == 3) else 0
                
            prev = curr
            