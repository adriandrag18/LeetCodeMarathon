# title: Longest ZigZag Path in a Binary Tree
# timestamp: 2024-12-30 15:03:42
# problemUrl: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# memory: 33.1 MB
# runtime: 61 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root, l=0, r=0):
            if root.left:
                self.res = max(self.res, r+1)
                dfs(root.left, l=r+1)
            if root.right:
                self.res = max(self.res, l+1)
                dfs(root.right, r=l+1)

        if root:
            dfs(root)
        return self.res