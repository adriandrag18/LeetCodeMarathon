# title: Cousins in Binary Tree
# timestamp: 2024-12-31 16:11:06
# problemUrl: https://leetcode.com/problems/cousins-in-binary-tree/
# memory: 17.8 MB
# runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root or root.val in [x, y]:
            return False
        
        lvl, newLvl, nums = [(root, None)], [], []
        while lvl:
            px, py = None, None
            for node, parent in lvl:
                if node.val == x:
                    px = parent
                if node.val == y:
                    py = parent
                if node.left:
                    newLvl.append((node.left, node))
                if node.right:
                    newLvl.append((node.right, node))
                
            lvl, newLvl, = newLvl, []
            if not px and not py:
                continue

            if px and py and px != py:
                return True
            
            return False

        
        return False