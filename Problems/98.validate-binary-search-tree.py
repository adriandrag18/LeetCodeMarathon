# title: Validate Binary Search Tree
# timestamp: 2024-12-21 10:33:23
# problemUrl: https://leetcode.com/problems/validate-binary-search-tree/
# memory: 19.8 MB
# runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(root):
            if not root.left and not root.right:
                return True, root.val, root.val
            
            mi, ma = root.val, root.val
            if root.left:
                res, minL, maxL = helper(root.left)
                if not res or root.val <= maxL:
                    return False, -1, -1
                mi = minL
            if root.right:
                res, minR, maxR = helper(root.right)
                if not res or minR <= root.val:
                    return False, -1, -1
                ma = maxR
            
            return True, mi, ma
        
        res, _, _ = helper(root)
        return res
