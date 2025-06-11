# title: Binary Tree Maximum Path Sum
# timestamp: 2025-05-20 12:14:41
# problemUrl: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# memory: 23 MB
# runtime: 18 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def helper(root):
            if not root:
                return 0
            
            nonlocal res
            l = max(0, helper(root.left))
            r = max(0, helper(root.right))
            
            res = max(res, root.val + l + r)
            return root.val + max(l, r)

        helper(root)
        return res