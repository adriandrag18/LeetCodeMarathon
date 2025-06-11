# title: Diameter of Binary Tree
# timestamp: 2024-12-19 18:15:00
# problemUrl: https://leetcode.com/problems/diameter-of-binary-tree/
# memory: 21.1 MB
# runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0, 0
            
            depthL, dimL = helper(root.left)
            depthR, dimR = helper(root.right)
            
            return 1 + max(depthL, depthR), max([dimL, dimR, depthL + depthR])
        
        if not root:
            return None
        
        _, dim = helper(root)
        return dim
