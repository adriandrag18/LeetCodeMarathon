# title: Lowest Common Ancestor of a Binary Tree
# timestamp: 2024-12-30 15:15:17
# problemUrl: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# memory: 22 MB
# runtime: 47 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        if l is not None and r is not None:
            return root
        
        return l if l is not None else r