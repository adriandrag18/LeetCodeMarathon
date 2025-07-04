# title: House Robber III
# timestamp: 2025-06-30 00:50:24
# problemUrl: https://leetcode.com/problems/house-robber-iii/
# memory: 20.1 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        root.notTaken = self.rob(root.left) + self.rob(root.right)
        root.taken = root.val + (root.left.notTaken if root.left else 0) + (root.right.notTaken if root.right else 0)
       
        return max(root.taken, root.notTaken)