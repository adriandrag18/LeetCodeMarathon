# title: Count Complete Tree Nodes
# timestamp: 2025-06-17 17:02:29
# problemUrl: https://leetcode.com/problems/count-complete-tree-nodes/
# memory: 23.3 MB
# runtime: 3 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)