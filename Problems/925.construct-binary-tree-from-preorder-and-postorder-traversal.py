# title: Construct Binary Tree from Preorder and Postorder Traversal
# timestamp: 2025-02-23 11:01:28
# problemUrl: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# memory: 17.9 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        val = preorder[0]
        root = TreeNode(val)
        if len(preorder) <=  1:
            return root
        
        leftval = preorder[1]
        rightval = postorder[-2]
        if leftval == rightval:
            root.left = self.constructFromPrePost(preorder[1:], postorder[:-1])
            return root

        indexLeftinPostorder = postorder.index(leftval)
        leftPostorder = postorder[:indexLeftinPostorder+1]
        rightPoastOrder = postorder[indexLeftinPostorder+1:-1]

        indexRightinPreorder = preorder.index(rightval)
        leftPreorder = preorder[1:indexRightinPreorder]
        rightPreorder = preorder[indexRightinPreorder:]
        
        # print(indexLeftinPostorder, indexRightinPreorder)
        # print(leftPostorder, rightPoastOrder)
        # print(leftPreorder, rightPreorder)
        
        root.left = self.constructFromPrePost(leftPreorder, leftPostorder)
        root.right = self.constructFromPrePost(rightPreorder, rightPoastOrder)

        return root