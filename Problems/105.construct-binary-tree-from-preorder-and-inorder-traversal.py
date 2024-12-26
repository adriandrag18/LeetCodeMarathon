# title: Construct Binary Tree from Preorder and Inorder Traversal
# timestamp: 2024-12-26 21:29:34
# problemUrl: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# memory: 89.3 MB
# runtime: 99 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # print(preorder, inorder)
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        i = inorder.index(root.val)
        # print(i)
 
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root
