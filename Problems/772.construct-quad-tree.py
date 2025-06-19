# title: Construct Quad Tree
# timestamp: 2025-06-19 15:07:47
# problemUrl: https://leetcode.com/problems/construct-quad-tree/
# memory: 18.5 MB
# runtime: 88 ms

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def const(x, y, m):
            val = grid[x][y]
            for i in range(x, x + m):
                for j in range(y, y + m):
                    if grid[i][j] != val:
                        half = m // 2
                        q1 = const(x, y, half)
                        q2 = const(x, y + half, half)
                        q3 = const(x + half, y, half)
                        q4 = const(x + half, y + half, half)
                        return Node(val, False, q1, q2, q3, q4)
            
            return Node(val, True, None, None, None, None)
        
        return const(0, 0, len(grid))