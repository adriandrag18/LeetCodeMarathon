# title: Delete Node in a BST
# timestamp: 2025-06-18 00:54:14
# problemUrl: https://leetcode.com/problems/delete-node-in-a-bst/
# memory: 21.4 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def getSmallest(root):
    if not root.left:
        return root.val
    return getSmallest(root.left)

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                smallest = getSmallest(root.right)
                root.val = smallest
                root.right = self.deleteNode(root.right, smallest)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:  # root.val > key
            root.left = self.deleteNode(root.left, key)
        
        return root
