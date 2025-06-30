# title: Construct Binary Tree from Inorder and Postorder Traversal
# timestamp: 2025-06-20 00:04:14
# problemUrl: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# memory: 18.8 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        dp = {val: i for i, val in enumerate(inorder)}
        def helper(l, r):
            if l == r:
                return None
            
            rootVal = postorder.pop()
            i = dp[rootVal]
            
            right = helper(i + 1, r)
            left = helper(l, i)
            return TreeNode(rootVal, left, right)
        
        return helper(0, len(inorder))
    