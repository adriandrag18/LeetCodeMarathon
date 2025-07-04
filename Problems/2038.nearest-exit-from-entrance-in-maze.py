# title: Nearest Exit from Entrance in Maze
# timestamp: 2025-01-06 16:21:09
# problemUrl: https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
# memory: 19.2 MB
# runtime: 64 ms

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        def getNeighbers(i, j):
            neighbers = []
            for i, j in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0 <= i < m and 0 <= j < n and maze[i][j] == '.':
                    neighbers.append((i, j))
            return neighbers

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = 's'
        while queue:
            i, j, depth = queue.popleft()
            for i, j in getNeighbers(i, j):
                if i == 0 or i == m -1 or j == 0 or j == n - 1:
                    return depth + 1
                queue.append((i, j, depth + 1))
                maze[i][j] = 's'
        
        return -1