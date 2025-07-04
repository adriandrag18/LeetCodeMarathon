# title: Binary Tree Inorder Traversal
# timestamp: 2024-12-31 15:21:27
# problemUrl: https://leetcode.com/problems/binary-tree-inorder-traversal/
# memory: 17.8 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
