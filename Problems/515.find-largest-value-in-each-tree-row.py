# title: Find Largest Value in Each Tree Row
# timestamp: 2024-12-26 00:04:24
# problemUrl: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# memory: 20 MB
# runtime: 1 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        lvl, newLvl = [root], []
        while lvl:
            for node in lvl:
                if node.left:
                    newLvl.append(node.left)
                if node.right:
                    newLvl.append(node.right)
            
            res.append(max([n.val for n in lvl]))
            lvl, newLvl = newLvl, []
        
        return res