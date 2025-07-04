# title: Kth Smallest Element in a BST
# timestamp: 2024-12-21 10:48:20
# problemUrl: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# memory: 21.1 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        
        def helper(root):
            if root.left:
                val = helper(root.left)
                if val >= 0:
                    return val
            
            if self.k == 1:
                return root.val
            self.k -= 1
            
            if root.right:
                val = helper(root.right)
                if val >= 0:
                    return val
            return -1

        return helper(root)
            