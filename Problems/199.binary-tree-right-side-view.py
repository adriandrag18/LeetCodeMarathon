# title: Binary Tree Right Side View
# timestamp: 2024-12-21 10:05:31
# problemUrl: https://leetcode.com/problems/binary-tree-right-side-view/
# memory: 18 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        lvl, newLvl, res = [root], [], []

        while lvl:
            res.append(lvl[-1].val)
            for node in lvl:
                if node.left:
                    newLvl.append(node.left)
                if node.right:
                    newLvl.append(node.right)
            lvl, newLvl = newLvl, []
        
        return res