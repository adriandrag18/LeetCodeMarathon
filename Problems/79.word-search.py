# title: Word Search
# timestamp: 2024-12-28 01:44:15
# problemUrl: https://leetcode.com/problems/word-search/
# memory: 17.7 MB
# runtime: 5020 ms

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        n, m = len(board), len(board[0])
        
        def helper(se, pos):
            # print(pos, se)
            if len(se) == len(word):
                return True

            for dir in dirs:
                i, j = pos[0] + dir[0], pos[1] + dir[1]
                # print(i, j)
                if not (0 <= i < n and 0 <= j < m):
                    continue
                if (i, j) in se or board[i][j] != word[len(se)]:
                    continue
                se.add((i, j))
                if helper(se, (i, j)):
                    return True
                se.remove((i, j))
            
            return False

        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if helper(set([(i, j)]), (i, j)):
                        return True
        
        return False
