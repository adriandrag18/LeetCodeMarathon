# title: Balanced Binary Tree
# timestamp: 2024-12-19 18:26:40
# problemUrl: https://leetcode.com/problems/balanced-binary-tree/
# memory: 18.9 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root: Optional[TreeNode]) -> (bool, int):
        if not root:
            return True, 0
        
        L, depthL = self.depth(root.left)
        if not L:
            return False, -1
        
        R, depthR = self.depth(root.right)
        if not R:
            return False, -1

        if abs(depthL - depthR) > 1:
            return False, -1
        
        return True, 1 + max(depthL, depthR)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        b, _ = self.depth(root)
        return b
        

