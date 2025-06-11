# title: Minimum Depth of Binary Tree
# timestamp: 2024-12-31 15:48:02
# problemUrl: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# memory: 49.7 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))