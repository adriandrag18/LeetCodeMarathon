# title: Range Sum of BST
# timestamp: 2024-12-31 16:36:45
# problemUrl: https://leetcode.com/problems/range-sum-of-bst/
# memory: 25.3 MB
# runtime: 3 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if high < root.val:
            return self.rangeSumBST(root.left, low, high)
        
        return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)