# title: Find Winner on a Tic Tac Toe Game
# timestamp: 2025-06-12 22:05:25
# problemUrl: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# memory: 17.7 MB
# runtime: 0 ms

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[''] * 3 for _ in range(3)]

        turn = 1
        for r, c in moves:
            board[r][c] = 'X' if turn else 'O'
            turn = 1 - turn

        for i in range(3):
            if board[i][0] and board[i][0] == board[i][1] == board[i][2]:
                return 'A' if board[i][0] == 'X' else 'B'
            if board[0][i] and board[0][i] == board[1][i] == board[2][i]:
                return 'A' if board[0][i] == 'X' else 'B'

        if board[1][1] and ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])):
            return 'A' if board[1][1] == 'X' else 'B'

        return 'Draw' if len(moves) == 9 else 'Pending'