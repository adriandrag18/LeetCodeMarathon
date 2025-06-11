# title: Flatten Binary Tree to Linked List
# timestamp: 2025-01-05 00:38:05
# problemUrl: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# memory: 18.2 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return None
        
        def helper(root, list):
            left, right = root.left, root.right
            for node in [left, right]:
                if node:
                    list.left, list.right = None, node
                    list = helper(list.right, list.right)
            
            return list
        
        helper(root, root)
        return root
