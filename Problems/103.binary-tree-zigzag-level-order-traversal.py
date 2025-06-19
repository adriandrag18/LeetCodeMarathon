# title: Binary Tree Zigzag Level Order Traversal
# timestamp: 2025-06-19 14:44:41
# problemUrl: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# memory: 17.9 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        lvls = []
        lvl, new = [root], []
        while lvl:
            for node in lvl:
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            lvls.append([node.val for node in lvl])
            lvl, new = new, []
        
        for lvl in lvls[1::2]:
            lvl.reverse()
        
        return lvls
                    