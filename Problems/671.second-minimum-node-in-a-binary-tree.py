# title: Second Minimum Node In a Binary Tree
# timestamp: 2025-01-02 11:51:31
# problemUrl: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# memory: 17.6 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minimum, secondMin = root.val, 10**11

        def dfs(root):
            nonlocal minimum, secondMin
            if root.left:
                if root.left.val > minimum:
                    secondMin = min(secondMin, root.left.val)
                    return
                dfs(root.left)
            if root.right:
                if root.right.val > minimum:
                    secondMin = min(secondMin, root.right.val)
                    return
                dfs(root.right)
        
        dfs(root)
        return secondMin if secondMin != 10**11 else -1
