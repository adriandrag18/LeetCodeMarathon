# title: Average of Levels in Binary Tree
# timestamp: 2025-06-17 23:43:04
# problemUrl: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# memory: 19.9 MB
# runtime: 3 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        lvl, newLvl, res = [root], [], []
        while lvl:
            total = 0
            for node in lvl:
                if node.left:
                    newLvl.append(node.left)
                if node.right:
                    newLvl.append(node.right)
                total += node.val
            res.append(total / len(lvl))
            lvl, newLvl = newLvl, []
        
        return res