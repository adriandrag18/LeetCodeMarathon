# title: Minimum Absolute Difference in BST
# timestamp: 2024-12-31 16:30:04
# problemUrl: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# memory: 19.6 MB
# runtime: 3 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = 100000
        prev = None
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            
            nonlocal prev
            if prev is not None:
                nonlocal res
                res = min(res, abs(prev - root.val))
            prev = root.val
            
            inorder(root.right)

        inorder(root)
        return res
