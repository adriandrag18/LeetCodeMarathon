# title: Count Good Nodes in Binary Tree
# timestamp: 2024-12-21 10:17:52
# problemUrl: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# memory: 32.2 MB
# runtime: 128 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(root, val):
            if val <= root.val:
                self.res += 1
                val = root.val
        
            if root.left:
                helper(root.left, val)
            if root.right:
                helper(root.right, val)
        
        self.res = 0
        helper(root, -100000)
        return self.res
        
