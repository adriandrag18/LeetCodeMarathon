# title: Lowest Common Ancestor of a Binary Search Tree
# timestamp: 2024-12-21 09:53:12
# problemUrl: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# memory: 21.2 MB
# runtime: 59 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small, large = min(p.val, q.val), max(p.val, q.val)
        while True:
            if large < root.val:
                root = root.left
                continue
            if root.val < small:
                root = root.right
                continue
            return root
        return root
