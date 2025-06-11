# title: Binary Tree Level Order Traversal
# timestamp: 2024-12-21 10:02:09
# problemUrl: https://leetcode.com/problems/binary-tree-level-order-traversal/
# memory: 18.6 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        lvl, newLvl, res = [root], [], []
        while lvl:
            res.append([n.val for n in lvl])
            
            for node in lvl:
                if node.left:
                    newLvl.append(node.left)
                if node.right:
                    newLvl.append(node.right)
            
            lvl, newLvl = newLvl, []
        
        return res