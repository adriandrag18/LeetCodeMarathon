# title: Valid Sudoku
# timestamp: 2024-11-01 12:38:29
# problemUrl: https://leetcode.com/problems/valid-sudoku/
# memory: 16.7 MB
# runtime: 11 ms

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row, col = [], []
            for j in range(9):
                row.append(board[i][j])
                col.append(board[j][i])
            if not self.isValid(row) or not self.isValid(col):
                print(row)
                print(col)
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        box.append(board[k][l])
                if not self.isValid(box):
                    print(box)
                    return False
        
        return True

    def isValid(self, l: List[str]) -> bool:
        
        nums = [int(el) for el in l if el != '.']
        if len(nums) == 0:
            
            return True

        if len(set(nums)) < len(nums) or min(nums) < 1 or max(nums) > 9:
            # print(nums)
            return False

        # print('true ', nums)

        return True
        