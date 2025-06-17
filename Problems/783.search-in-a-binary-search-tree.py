# title: Search in a Binary Search Tree
# timestamp: 2025-06-18 00:50:54
# problemUrl: https://leetcode.com/problems/search-in-a-binary-search-tree/
# memory: 19 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            if root.val < val:
                root = root.right
            else:
                root = root.left
        
        return root