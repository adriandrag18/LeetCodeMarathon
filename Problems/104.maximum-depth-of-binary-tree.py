# title: Maximum Depth of Binary Tree
# timestamp: 2024-12-19 18:08:10
# problemUrl: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# memory: 18.9 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))